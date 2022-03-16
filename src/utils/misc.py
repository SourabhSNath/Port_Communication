from PyQt6 import QtWidgets
from mysql.connector import errorcode


def call_error_msg_box(message):
    msg = QtWidgets.QMessageBox()
    msg.setText(message)
    msg.setWindowTitle("Error")
    msg.exec()


def handle_db_exception(e, logger):
    if e.errno == errorcode.CR_CONNECTION_ERROR or e.errno == errorcode.CR_CONN_HOST_ERROR:
        error_msg = f"{e.msg}"
        logger.error(f"error message {error_msg}, e {e}")
        call_error_msg_box(error_msg)

    elif e.errno == errorcode.CR_UNKNOWN_HOST:
        error_msg = "Cannot connect to the host. Please check if the host is available."
        logger.error(f"error message {error_msg}, e {e}")
        call_error_msg_box(error_msg)
    else:
        logger.error(f"Error {e}")
        call_error_msg_box(f"Unknown error: {e}")

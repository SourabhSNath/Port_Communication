import mysql.connector
from PyQt6 import QtWidgets

from src.Constants import DB_CREDENTIALS_FILE
from src.data.database.device_database import DeviceDatabase
from src.db_info_window import DatabaseInfoWindow
from src.gui import tabbed_main_communication_window
from src.main.ethernet_tab import EthernetTab
from src.main.serial_tab import SerialTab
from src.utils import file_operations
from src.utils.misc import handle_db_exception
from src.utils.uncaught_exception_hook import UncaughtHook

"""
# Main window. Run this file to see the app.
"""

logger = file_operations.setup_logging("app.log")


class MainWindow(QtWidgets.QMainWindow, tabbed_main_communication_window.Ui_MainWindow):
    # List of previously read messages. Class variable for now.
    previous_read_data_list = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.serial_tab_controller = SerialTab(parent=self.serial_tab, statusbar=self.statusbar)
        self.serial_tab.layout().addWidget(self.serial_tab_controller)

        self.ethernet_tab_controller = EthernetTab(parent=self.ethernet_tab, statusbar=self.statusbar)
        self.ethernet_tab.layout().addWidget(self.ethernet_tab_controller)


def main():
    import sys
    qt_exception_hook = UncaughtHook()

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Port Communication")
    try:
        # If the credential file does not exist open the dialog window to enter new information to connect with the
        # database
        if not file_operations.file_exists(DB_CREDENTIALS_FILE):
            db = DeviceDatabase()
            DatabaseInfoWindow(database=db).exec()
            # Close the database connection here. Otherwise table won't be updated in the main window.
            db.close_database_connection()
            del db
    except mysql.connector.Error as e:
        logger.exception(e)
        handle_db_exception(e, logger)
    form = MainWindow()
    form.show()
    app.exec()


if __name__ == "__main__":
    main()

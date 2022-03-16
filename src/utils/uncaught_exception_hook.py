import sys
import traceback
from types import TracebackType

from PyQt6 import QtWidgets
from PyQt6.QtCore import QObject, pyqtSignal
from loguru import logger

"""
Class to detect any uncaught exceptions that may occur.
"""


class UncaughtHook(QObject):
    _exception_caught = pyqtSignal(object)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # this registers the exception_hook() function as hook with the Python interpreter
        sys.excepthook = self.exception_hook

    def exception_hook(self, exception_type, exception_value, exception_traceback: TracebackType):

        """Function handling uncaught exceptions.
         It is triggered each time an uncaught exception occurs.
         """
        if issubclass(exception_type, KeyboardInterrupt):
            # ignore keyboard interrupt to support console applications
            sys.__excepthook__(exception_type, exception_value, exception_traceback)
        else:
            msg = '\n'.join(
                [''.join(traceback.format_tb(exception_traceback)),
                 '{0}: {1}'.format(exception_type.__name__, exception_value)]
            )
            print(msg)
            logger.opt(exception=(exception_type, exception_value, exception_traceback)).critical("Unhandled Qt Error",
                                                                                                  msg)

            # # trigger message box show
            # self._exception_caught.emit(log_msg)


def show_exception_box(log_msg):
    """Checks if a QApplication instance is available and shows a messagebox with the exception message.
    If unavailable (non-console application), log an additional notice.
    """
    if QtWidgets.QApplication.instance() is not None:
        errorbox = QtWidgets.QMessageBox()
        errorbox.setText("Oops. An unexpected error occured:\n{0}".format(log_msg))
        errorbox.exec()
    else:
        logger.debug("Uncaught Exception Hook. No QApplication instance available to show the error.")

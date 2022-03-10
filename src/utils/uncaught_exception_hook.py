import sys
import sys
import traceback

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

    def exception_hook(self, exc_type, exc_value, exc_traceback):

        """Function handling uncaught exceptions.
         It is triggered each time an uncaught exception occurs.
         """
        if issubclass(exc_type, KeyboardInterrupt):
            # ignore keyboard interrupt to support console applications
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
        else:
            # exc_info = (exc_type, exc_value, exc_traceback)
            # log_msg = '\n'.join([''.join(traceback.format_tb(exc_traceback)),
            #                      '{0}: {1}'.format(exc_type.__name__, exc_value)])
            # logger.critical("Uncaught exception:\n {0}".format(log_msg), exc_info=exc_info)

            msg = traceback.format_tb(exc_type.__name__, exc_value)
            logger.opt(exception=(exc_type, exc_value, exc_traceback)).error("Unhandled Qt Error", msg)

            # # trigger message box show
            # self._exception_caught.emit(log_msg)

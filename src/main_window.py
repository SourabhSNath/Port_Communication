from PyQt6 import QtWidgets
from gui import main_communication_window

import serial_communication


class MainWindow(QtWidgets.QMainWindow, main_communication_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Avionics Protocol System")

    form = MainWindow()
    form.show()
    app.exec()

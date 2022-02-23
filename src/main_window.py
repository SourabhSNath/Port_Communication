from PyQt6 import QtWidgets

import serial_communication
from gui import main_communication_window


class MainWindow(QtWidgets.QMainWindow, main_communication_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_baud_rate()
        self.search_device_button.clicked.connect(self.search_devices)

    # Set Baud rates programmatically since the numbers aren't known.
    def setup_baud_rate(self):
        baud_rates = [110, 150, 300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600]
        self.baud_rate_combo_box.clear()  # Clearing the default 110 set in the ui file inorder to prevent 2 copies.
        for rate in baud_rates:
            self.baud_rate_combo_box.addItem(str(rate))

    def search_devices(self):
        serial_devices = serial_communication.get_all_devices()
        for i in serial_devices:
            for key in i:
                if key == "Device":
                    self.device_combox_box.addItem(i[key])
                if key == "Port Name":
                    self.port_input.setText(i[key])
                if key == "Serial Number":
                    self.serial_no_input.setText(i[key])
                if key == "Port":
                    serial_communication.port_location = (i[key])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Avionics Protocol System")

    form = MainWindow()
    form.show()
    app.exec()

from PyQt6 import QtWidgets

from gui import main_communication_window
# import serial_communication
from serial_communication import SerialCommunication


class MainWindow(QtWidgets.QMainWindow, main_communication_window.Ui_MainWindow):
    previous_read_data = ""

    def __init__(self):
        super().__init__()
        self.serial_communication = SerialCommunication()
        self.setupUi(self)
        self.serial_devices = []
        self.current_device = {}
        self.is_device_found = False
        self.is_device_connected = False
        self.setup_baud_rate()
        self.search_device_button.clicked.connect(self.search_devices)
        self.connect_button.clicked.connect(self.serial_connection)
        self.send_message_button.clicked.connect(self.write_to_device)

    # Set Baud rates programmatically since the numbers aren't known.
    def setup_baud_rate(self):
        baud_rates = [110, 150, 300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600]
        self.baud_rate_combo_box.clear()  # Clearing the default 110 set in the ui file inorder to prevent 2 copies.
        for rate in baud_rates:
            self.baud_rate_combo_box.addItem(str(rate))

    # Search all serial communication devices connected to the system
    def search_devices(self):
        self.serial_devices = self.serial_communication.get_all_devices()
        for i in self.serial_devices:
            for key in i:
                if key == "Device":
                    self.device_combox_box.addItem(i[key])
                if key == "Port Name":
                    self.port_input.setText(i[key])
                if key == "Serial Number":
                    self.serial_no_input.setText(i[key])
                # if key == "Port":
                #     serial_communication.port_location = (i[key])

        if len(self.serial_devices) != 0:
            self.is_device_found = True

    # Connect to the device currently seen in the combobox, currently connects to the first serial_device list item
    # in the combo box.
    # TODO: Get the id of the device when the user selects another device in the list through the combobox
    def serial_connection(self):
        if self.serial_devices:
            if self.connect_button.text() == "Connect":
                self.connect_button.setText("Disconnect")
                device_name = self.device_combox_box.currentText()
                if self.is_device_found:
                    MainWindow.current_device = current_device = self.serial_devices[0]
                    if current_device["Device"] == device_name:
                        self.serial_communication.connection(current_device["Port"],
                                                             self.baud_rate_combo_box.currentText())
                        self.is_device_connected = self.serial_communication.get_connection_status()
            else:
                self.connect_button.setText("Connect")
        else:
            call_error_msg_box("Please select a device.")

    def write_to_device(self):
        if self.is_device_connected:
            message = self.send_message_input.toPlainText()
            print("Send to device", message)
            self.serial_communication.write_data(message)
            # This needs to be automatic by using threading or some observer pattern, here it just checks the
            # previous value and makes changes if only the new value is different.
            if self.serial_communication.received_data != MainWindow.previous_read_data:
                MainWindow.previous_read_data = self.serial_communication.received_data
                self.update_received_message(self.serial_communication.received_data)
            self.send_message_input.clear()
        else:
            call_error_msg_box("Please check if the device is connected.")

    def update_received_message(self, msg):
        self.recieved_message_text_output.append(msg.decode("utf-8"))


def call_error_msg_box(message):
    msg = QtWidgets.QMessageBox()
    msg.setText(message)
    msg.setWindowTitle("Error")
    msg.exec()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Avionics Protocol System")

    form = MainWindow()
    form.show()
    app.exec()

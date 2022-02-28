from PyQt6 import QtWidgets

import file_operations
from device_database import DeviceDatabase
from gui import main_communication_window
from save_window import SaveDialogWindow
from serial_communication import SerialCommunication
# Main window. Run this file to see the app.
from src.data.serial_device import Parity, SerialDevice


class MainWindow(QtWidgets.QMainWindow, main_communication_window.Ui_MainWindow):
    # List of previously read messages. Class variable for now.
    previous_read_data_list = []

    def __init__(self):
        super().__init__()
        self.current_device = None
        self.serial_communication = SerialCommunication()
        self.setupUi(self)
        self.db = DeviceDatabase()
        self.serial_devices = []
        self.is_device_found = False
        self.setup_table()
        self.is_device_connected = False
        self.setup_baud_rate()
        self.update_table()
        self.save_dialog = SaveDialogWindow()
        self.search_device_button.clicked.connect(self.search_devices)
        self.connect_button.clicked.connect(self.serial_connection)
        self.send_message_button.clicked.connect(self.write_to_device)
        self.save_to_database_button.clicked.connect(self.save_data)
        self.action_export_data.triggered.connect(self.export_table_data)
        self.action_load_data.triggered.connect(self.load_table_data_from_file)
        self.action_delete_data.triggered.connect(self.delete_data_from_table)

    def setup_table(self):
        self.saved_table.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        column_count = 7
        self.saved_table.setColumnCount(column_count)
        self.saved_table.setHorizontalHeaderLabels(
            ["Device Name", "Product Name", "Serial Number", "Baud Rate", "Priority Bits", "Data Bits", "Port Name"])
        header = self.saved_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        self.saved_table.setStyleSheet("QTableWidget::item {padding: 8px}")
        self.saved_table.verticalHeader().setVisible(False)

        self.saved_table.doubleClicked.connect(self.on_table_double_click)

    def on_table_double_click(self):
        idx = self.saved_table.selectionModel().selectedIndexes()[0]
        row = idx.row()
        print(idx.row())
        self.device_combox_box.clear()
        for col in range(7):
            print("Col", col)
            if col == 0:
                device_name = self.get_table_data(row, col)
                product_name = self.get_table_data(row, col + 1)
                if device_name == product_name:
                    self.device_combox_box.addItem(f"{device_name}")
                else:
                    self.device_combox_box.addItem(f"{device_name} [{product_name}]")
                col += 1
            elif col == 2:
                self.serial_no_input.setText(self.get_table_data(row, col))
            elif col == 3:
                self.baud_rate_combo_box.setCurrentText(self.get_table_data(row, col))
            elif col == 4:
                self.parity_combobox.setCurrentText(self.get_table_data(row, col))
            elif col == 5:
                self.data_bit_combobox.setCurrentText(self.get_table_data(row, col))
            else:
                self.port_input.setText(self.get_table_data(row, col))

    def get_table_data(self, row, col):
        print("ROW", row, "Col", col)
        text = self.saved_table.item(row, col).text()
        print(text)
        return text

    # Set Baud rates programmatically since the numbers aren't known.
    def setup_baud_rate(self):
        baud_rates = [110, 150, 300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600]
        self.baud_rate_combo_box.clear()  # Clearing the default 110 set in the ui file inorder to prevent 2 copies.
        for rate in baud_rates:
            self.baud_rate_combo_box.addItem(str(rate))

    # Search all serial communication devices connected to the system
    def search_devices(self):
        self.serial_devices = self.serial_communication.get_all_devices()
        print("SerialDevices", self.serial_devices)
        self.statusbar.showMessage("Searching")

        for device in self.serial_devices:
            self.device_combox_box.addItem(device.product_name)
            self.port_input.setText(device.port_name)
            self.serial_no_input.setText(device.serial_number)

        if len(self.serial_devices) != 0:
            self.is_device_found = True
            self.current_device = self.serial_devices[0]  # Set the first device as the current device.
            self.statusbar.showMessage("Device Found", msecs=1500)
        else:
            self.statusbar.showMessage("No devices found.")

    def handle_device_name_clicks(self):
        pass

    # Connect to the device currently seen in the combobox, currently connects to the first serial_device list item
    # in the combo box.
    # TODO: Get the id of the device when the user selects another device in the list through the combobox
    def serial_connection(self):
        if self.serial_devices:
            if self.connect_button.text() == "Connect":
                self.connect_button.setText("Disconnect")
                device_name = self.device_combox_box.currentText()
                if self.is_device_found:
                    self.current_device = self.serial_devices[0]  # TODO: Handle device selection here
                    if self.current_device.device_name == device_name:
                        self.serial_communication.connection(self.current_device.port,
                                                             self.baud_rate_combo_box.currentText(),
                                                             self.parity_combobox.currentText(),
                                                             int(self.data_bit_combobox.currentText()))
                        self.is_device_connected = self.serial_communication.get_connection_status()
                        print("IS Device Connected", self.is_device_connected)
                        self.statusbar.showMessage("Connecting to device", msecs=500)
            else:
                self.connect_button.setText("Connect")
                self.statusbar.showMessage("Disconnect", msecs=1500)
        else:
            call_error_msg_box("Please select a device.")

    # Send message to device.
    def write_to_device(self):
        if self.is_device_connected:
            message = self.send_message_input.toPlainText()
            print("Send to device", message)
            self.serial_communication.write_data(message)
            self.statusbar.showMessage("Sending", msecs=400)
            # This needs to be automatic by using threading or some observer pattern, here it just checks the
            # previous value and makes changes if only the new value is different.
            if self.serial_communication.received_data_list != MainWindow.previous_read_data_list:
                MainWindow.previous_read_data_list = self.serial_communication.received_data_list[:]
                print("MainWindow previous_read_data_list", MainWindow.previous_read_data_list)
                for msg in MainWindow.previous_read_data_list:
                    self.update_received_message(msg)
                self.send_message_input.clear()
            else:
                call_error_msg_box("Please enter a message.")
        else:
            call_error_msg_box("Please check whether the device is connected.")

    def update_received_message(self, msg):
        self.recieved_message_text_output.append(msg.decode("utf-8"))

    def save_data(self):
        product_name = self.device_combox_box.currentText()
        if product_name:
            baud_rate = self.baud_rate_combo_box.currentText()
            parity = self.parity_combobox.currentText()
            data_bits = self.data_bit_combobox.currentText()

            if self.current_device is not None:
                self.current_device.baud_rate = int(baud_rate)
                if parity == "No Parity":
                    self.current_device.parity = Parity.NO_PARITY
                elif parity == "Even":
                    self.current_device.parity = Parity.EVEN
                else:
                    self.current_device.parity = Parity.ODD

                self.current_device.data_bits = data_bits
                self.save_dialog.open_save_data_window(db=self.db, serial_device=self.current_device)

                self.update_table()
            else:
                print("Current device is none")
        else:
            call_error_msg_box("Please check the inputs.")

    def update_table(self):
        results = self.db.get_table_data()
        print("Table Data:", results)
        if results is not None:
            self.saved_table.setRowCount(len(results))
            for row_count, row_data in enumerate(results):
                for col_count, col_data in enumerate(row_data):

                    # Skipping index and interface from the table widget.
                    if col_count != 0 and col_count != 4:
                        if col_count == 6:  # If it is the parity column
                            if col_data == '0':
                                parity = "Odd"
                            elif col_data == 'E':
                                parity = "Even"
                            else:
                                parity = "No Parity"
                            # Decreasing column count by 2 since we do not want to show the index and the interface in table
                            self.saved_table.setItem(row_count, col_count - 2, QtWidgets.QTableWidgetItem(parity))
                        else:
                            print("DATA", str(col_data), end=",")
                            if col_count < 4:
                                self.saved_table.setItem(row_count, col_count - 1,
                                                         QtWidgets.QTableWidgetItem(str(col_data)))
                            else:
                                # Decreasing by 2 since it is after the interface data
                                self.saved_table.setItem(row_count, col_count - 2,
                                                         QtWidgets.QTableWidgetItem(str(col_data)))

    # Export Table Data to a folder of user choice.
    def export_table_data(self):
        result = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "export_table_data.json", filter="*.json")
        folder_path = result[0]
        if folder_path:
            data = self.db.get_table_data_dictionary()
            file_operations.export_table_data(folder_path, data)

    # Load table data from a file chosen by the user.
    def load_table_data_from_file(self):
        result = QtWidgets.QFileDialog.getOpenFileNames(self, filter="*.json")[0]
        if result:
            data_list_dict = file_operations.import_table_data(result[0])
            # progress = QtWidgets.QProgressDialog("Importing data")
            # progress.show()
            for count, dict_item in enumerate(data_list_dict):
                loaded_serial_device = SerialDevice(device_name=dict_item["device_name"],
                                                    product_name=dict_item["device_name"],
                                                    serial_number=dict_item["serial_number"],
                                                    baud_rate=dict_item["baud_rate"], parity=dict_item["parity_bits"],
                                                    data_bits=dict_item["data_bits"], port_name=dict_item["port_name"],
                                                    port=dict_item["port"], interface=dict_item["interface"]
                                                    )
                self.db.insert_data(loaded_serial_device)
            self.update_table()

    def delete_data_from_table(self):
        self.db.delete_table()
        self.update_table()


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

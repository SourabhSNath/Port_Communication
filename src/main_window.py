from PyQt6 import QtWidgets

import file_operations
from device_database import DeviceDatabase
from gui import main_communication_window
from save_window import SaveDialogWindow
from serial_communication import SerialCommunication


class MainWindow(QtWidgets.QMainWindow, main_communication_window.Ui_MainWindow):
    # List of previously read messages. Class variable for now.
    previous_read_data_list = []

    def __init__(self):
        super().__init__()
        self.serial_communication = SerialCommunication()
        self.setupUi(self)
        self.db = DeviceDatabase()
        self.serial_devices = []
        self.current_device = {}  # TO keep track of the current device. Unused for now.
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
        self.statusbar.showMessage("Searching")
        for i in self.serial_devices:
            for key in i:
                if key == "Device":
                    self.device_combox_box.clear()
                    self.device_combox_box.addItem(i[key])
                if key == "Port Name":
                    self.port_input.setText(i[key])
                if key == "Serial Number":
                    self.serial_no_input.setText(i[key])

        if len(self.serial_devices) != 0:
            self.is_device_found = True
            self.statusbar.showMessage("Device Found", msecs=1500)
        else:
            self.statusbar.showMessage("No devices found.")

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
                        print("IS Device Connected", self.is_device_connected)
                        self.statusbar.showMessage("Connecting to device", msecs=500)
            else:
                self.connect_button.setText("Connect")
                self.statusbar.showMessage("Disconnect", msecs=1500)
        else:
            call_error_msg_box("Please select a device.")

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
            port_name = self.port_input.text()
            serial_number = self.serial_no_input.text()
            baud_rate = self.baud_rate_combo_box.currentText()
            parity = self.parity_combobox.currentText()
            data_bits = self.data_bit_combobox.currentText()
            self.save_dialog.open_save_data_window(db=self.db, product_name=product_name, port_name=port_name,
                                                   serial_number=serial_number,
                                                   baud_rate=baud_rate, parity=parity, data_bits=data_bits)

            self.update_table()
        else:
            call_error_msg_box("Please check the inputs.")

    def update_table(self):
        results = self.db.get_table_data()
        print("Table Data:", results)
        self.saved_table.setRowCount(len(results))
        for row_count, row_data in enumerate(results):
            for col_count, data in enumerate(row_data):

                # Skipping index from the table.
                if col_count != 0:
                    if col_count == 5:
                        if data == '0':
                            parity = "Odd"
                        elif data == 'E':
                            parity = "Even"
                        else:
                            parity = "No Parity"
                        # Decreasing column count by 1 since we do not want to show the index
                        self.saved_table.setItem(row_count, col_count - 1, QtWidgets.QTableWidgetItem(parity))
                    else:
                        self.saved_table.setItem(row_count, col_count - 1, QtWidgets.QTableWidgetItem(str(data)))

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
                self.db.insert_data(dict_item["device_name"], dict_item["product_name"], dict_item["serial_number"],
                                    dict_item["baud_rate"], dict_item["parity_bits"], dict_item["data_bits"],
                                    dict_item["port_name"])

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

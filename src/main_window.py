import os.path

from PyQt6 import QtWidgets, QtCore
from loguru import logger

import file_operations
from gui import main_communication_window
from save_window import SaveDialogWindow
from serial_communication import SerialCommunication, DataSignal
from src.Constants import DB_CREDENTIALS_FILE
from src.data.database.device_database import DeviceDatabase
from src.data.model.serial_device import Parity, SerialDevice
from src.db_info_window import DatabaseInfoWindow

"""
# Main window. Run this file to see the app.
"""

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Logs", "main_window.log")
logger.add(path, rotation="250MB", encoding="utf-8")


class MainWindow(QtWidgets.QMainWindow, main_communication_window.Ui_MainWindow):
    # List of previously read messages. Class variable for now.
    previous_read_data_list = []

    def __init__(self):
        super().__init__()
        self.current_device = None
        self.setupUi(self)
        self.serial_communication = SerialCommunication()
        self.serial_communication_signal = self.serial_communication.data_signal.read_message_signal
        self.serial_communication_signal.connect(self.update_received_message)
        try:
            self.db = DeviceDatabase()
        except:
            pass
        self.serial_devices = []
        self.is_device_found = False
        self.selected_table_row_index = -1  # Index that will be updated when the table row is double clicked
        self.setup_table()
        self.is_device_connected = False
        self.setup_baud_rate()
        try:
            self.update_table()
        except:
            pass
        self.save_dialog = SaveDialogWindow()
        self.device_combox_box.currentIndexChanged.connect(self.on_device_combox_box_item_change)
        self.search_device_button.clicked.connect(self.search_devices)
        self.connect_button.clicked.connect(self.serial_connection)
        self.send_message_button.clicked.connect(self.write_to_device)
        self.save_to_database_button.clicked.connect(self.save_data)
        self.action_export_data.triggered.connect(self.export_table_data)
        self.action_load_data.triggered.connect(self.load_table_data_from_file)
        self.action_delete_data.triggered.connect(self.delete_data_from_table)
        self.action_database_credentials.triggered.connect(self.open_credential_window)

    # Change the combox box items when the user selects a different device from the results
    def on_device_combox_box_item_change(self):
        if self.selected_table_row_index == -1:
            self.current_device = self.serial_devices[self.device_combox_box.currentIndex()]
            logger.info("Current Device: {}", self.current_device)
            self.port_input.setText(self.current_device.port_name)
            self.serial_no_input.setText(self.current_device.serial_number)
            self.baud_rate_combo_box.setCurrentText(str(self.current_device.baud_rate))
            self.parity_combobox.setCurrentText(self.current_device.get_parity_string())
            self.data_bit_combobox.setCurrentText(str(self.current_device.data_bits))

    def setup_table(self):
        self.saved_table.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        column_count = 8
        self.saved_table.setColumnCount(column_count)
        self.saved_table.setHorizontalHeaderLabels(
            ["ID", "Device Name", "Product Name", "Serial Number", "Baud Rate", "Parity Bits", "Data Bits",
             "Port Name"])
        header = self.saved_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.saved_table.setColumnHidden(0, True)

        self.saved_table.setStyleSheet("QTableWidget::item {padding: 8px}")
        self.saved_table.verticalHeader().setVisible(False)

        self.saved_table.doubleClicked.connect(self.on_table_double_click)

    def on_table_double_click(self):
        idx = self.saved_table.selectionModel().selectedIndexes()[0]
        row = idx.row()
        self.device_combox_box.clear()
        # Immediately set to 0 to prevent on_device_combox_box_item_change from being triggered
        self.selected_table_row_index = 0
        for col in range(8):
            print(col, self.get_table_data(row, col))
            if col == 0:
                # Get the Database Table Row index from the hidden column's row
                self.selected_table_row_index = self.get_table_data(row, col)
            if col == 1:
                device_name = self.get_table_data(row, col)
                product_name = self.get_table_data(row, col + 1)
                print(device_name, product_name)
                if device_name == product_name:
                    self.device_combox_box.addItem(f"{device_name}")
                else:
                    self.device_combox_box.addItem(f"{device_name} [{product_name}]")
                col += 1
            elif col == 3:
                self.serial_no_input.setText(self.get_table_data(row, col))
            elif col == 4:
                self.baud_rate_combo_box.setCurrentText(self.get_table_data(row, col))
            elif col == 5:
                self.parity_combobox.setCurrentText(self.get_table_data(row, col))
            elif col == 6:
                self.data_bit_combobox.setCurrentText(self.get_table_data(row, col))
            elif col == 7:
                self.port_input.setText(self.get_table_data(row, col))
        self.save_to_database_button.setText("Save Edit")

    def get_table_data(self, row, col):
        text = self.saved_table.item(row, col).text()
        return text

    # Set Baud rates programmatically since the numbers aren't known.
    def setup_baud_rate(self):
        baud_rates = [110, 150, 300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600]
        self.baud_rate_combo_box.clear()  # Clearing the default 110 set in the ui file inorder to prevent 2 copies.
        for rate in baud_rates:
            self.baud_rate_combo_box.addItem(str(rate))

    # Search all serial communication devices connected to the system
    def search_devices(self):
        self.device_combox_box.clear()
        self.serial_devices.clear()
        self.save_to_database_button.setText("Save")
        self.serial_devices = self.serial_communication.get_all_devices()
        print(f"Searched Devices {self.serial_devices}")
        self.statusbar.showMessage("Searching")
        self.selected_table_row_index = -1  # Reset to -1 since no table row is being selected

        for device in self.serial_devices:
            self.device_combox_box.addItem(device.product_name)

        if len(self.serial_devices) != 0:
            self.is_device_found = True
            self.current_device = self.serial_devices[0]  # Set the first device as the current device.
            self.port_input.setText(self.current_device.port_name)
            self.serial_no_input.setText(self.current_device.serial_number)
            self.statusbar.showMessage("Device Found", msecs=1500)
        else:
            self.statusbar.showMessage("No devices found.")

    def handle_device_name_clicks(self):
        pass

    # Connect to the device currently seen in the combobox, currently connects to the first serial_device list item
    # in the combo box.
    def serial_connection(self):
        if self.serial_devices:
            if self.connect_button.text() == "Connect":
                self.connect_button.setText("Disconnect")
                self.search_device_button.setDisabled(True)
                device_name = self.device_combox_box.currentText()
                index = self.device_combox_box.currentIndex()
                if self.is_device_found and self.current_device is not None:
                    self.current_device = self.serial_devices[index]
                    print("Connect Device: ", self.current_device)
                    print(self.current_device.product_name, device_name)
                    if self.current_device.product_name == device_name:
                        self.serial_communication.connection(self.current_device.port_name,
                                                             self.baud_rate_combo_box.currentText(),
                                                             self.parity_combobox.currentIndex(),
                                                             int(self.data_bit_combobox.currentText()),
                                                             self.current_device.product_name)
                        self.is_device_connected = self.serial_communication.get_connection_status()
                        print("IS Device Connected", self.is_device_connected)
                        self.statusbar.showMessage("Connecting to device", msecs=500)
                else:
                    logger.error(
                        "Serial device not connected. Is Device Found: {} Current Device: {}", self.is_device_found,
                        self.current_device)
            else:
                self.serial_communication.close_connection()
                self.search_device_button.setDisabled(False)
                self.connect_button.setText("Connect")
                self.statusbar.showMessage("Disconnect", msecs=1500)
        else:
            call_error_msg_box("Please select a device.")

    # Send message to device.
    def write_to_device(self):
        if self.is_device_connected:
            self.send_message_input.setAcceptRichText(False)
            message = self.send_message_input.toPlainText()
            # print("Send to device", message)
            # self.serial_communication.write_data(message)
            self.statusbar.showMessage("Sending", msecs=400)
            if message:
                # TODO: REMOVE MANUAL \r after testing end of line or different codes with actual serial device
                self.serial_communication.write_data(message + "\r")
                # This needs to be automatic by using threading or some observer pattern, here it just checks the
                # previous value and makes changes if only the new value is different.
                # if self.serial_communication.received_data_list:
                #     if self.serial_communication.received_data_list != MainWindow.previous_read_data_list:
                #         MainWindow.previous_read_data_list = self.serial_communication.received_data_list[:]
                #         for msg in MainWindow.previous_read_data_list:
                #             self.update_received_message(msg)
                #         self.send_message_input.clear()
                #     else:
                #         call_error_msg_box("Please enter a message.")
                # else:
                #     call_error_msg_box("No data received. Please check your device.")
            else:
                call_error_msg_box("Please enter a message.")
        else:
            call_error_msg_box("Please check whether the device is connected.")

    @QtCore.pyqtSlot(str)
    def update_received_message(self, msg):
        print(msg)
        if msg:
            self.recieved_message_text_output.append(msg)
        else:
            call_error_msg_box("N")

    def save_data(self):
        product_name = self.device_combox_box.currentText()
        if product_name:
            baud_rate = self.baud_rate_combo_box.currentText()
            parity_text = self.parity_combobox.currentText()
            data_bits = self.data_bit_combobox.currentText()
            port_name = self.port_input.text()
            if parity_text == "No Parity":
                parity = Parity.NO_PARITY
            elif parity_text == "Even":
                parity = Parity.EVEN
            else:
                parity = Parity.ODD

            if self.current_device is not None and self.selected_table_row_index == -1:
                self.current_device.baud_rate = int(baud_rate)
                self.current_device.parity = parity
                self.current_device.data_bits = data_bits
                self.save_dialog.open_save_data_window(db=self.db, serial_device=self.current_device)
            else:
                self.save_dialog.open_save_data_window(db=self.db, id=self.selected_table_row_index,
                                                       product_name=product_name, baud_rate=baud_rate, parity=parity,
                                                       data_bits=data_bits, port_name=port_name)

            self.update_table()
        else:
            call_error_msg_box("Please check the inputs.")

    def update_table(self):
        if self.db is not None:
            results = self.db.get_table_data()
            print("Table Data:", results)
            if results is not None:
                self.saved_table.setRowCount(len(results))
                for row_count, row_data in enumerate(results):
                    for col_count, col_data in enumerate(row_data):
                        if col_count != 4:
                            if col_count == 6:
                                if col_data == 'O':
                                    parity = "Odd"
                                elif col_data == 'E':
                                    parity = "Even"
                                else:
                                    parity = "No Parity"
                                self.saved_table.setItem(row_count, col_count - 1, QtWidgets.QTableWidgetItem(parity))
                            else:
                                if col_count < 4:
                                    self.saved_table.setItem(row_count, col_count,
                                                             QtWidgets.QTableWidgetItem(str(col_data)))
                                else:
                                    self.saved_table.setItem(row_count, col_count - 1,
                                                             QtWidgets.QTableWidgetItem(str(col_data)))

    # Export Table Data to a folder of user choice.
    def export_table_data(self):
        result = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "export_table_data.json", filter="*.json")
        folder_path = result[0]
        if folder_path:
            data = self.db.get_table_data_dictionary()
            file_operations.export_data_to_json(folder_path, data)

    # Load table data from a file chosen by the user.
    def load_table_data_from_file(self):
        result = QtWidgets.QFileDialog.getOpenFileNames(self, filter="*.json")[0]
        if result:
            data_list_dict = file_operations.import_data_from_json(result[0])
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

    def open_credential_window(self):
        credential_window = DatabaseInfoWindow()
        credential_window.open_window(self.db)

    def delete_data_from_table(self):
        self.db.delete_table()
        self.update_table()

    def open_db_info_window(self):
        DatabaseInfoWindow(database=self.db).exec()


def call_error_msg_box(message):
    msg = QtWidgets.QMessageBox()
    msg.setText(message)
    msg.setWindowTitle("Error")
    msg.exec()


def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Port Communication")
    try:
        db = DeviceDatabase()

        # If the credential file does not exist open the dialog window to enter new information to connect with the database
        if not file_operations.file_exists(DB_CREDENTIALS_FILE):
            DatabaseInfoWindow(database=db).exec()
        # Close the database connection here. Otherwise table won't be updated in the main window.
        db.close_database_connection()
        del db
    except:
        pass
    form = MainWindow()
    form.show()
    app.exec()


if __name__ == "__main__":
    main()

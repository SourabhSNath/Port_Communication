from typing import Optional

from PyQt6 import QtWidgets

from gui import save_window_ui
from src.data.database.device_database import DeviceDatabase
from src.data.model.serial_device import SerialDevice


# Dialog window that handles save operations.
class SaveDialogWindow(QtWidgets.QDialog, save_window_ui.Ui_Dialog):
    db: DeviceDatabase = None

    def __init__(self):
        super(SaveDialogWindow, self).__init__()
        self.port_name = None
        self.data_bits = None
        self.parity = None
        self.baud_rate = None
        self.product_name = None
        self.db_id = None
        self.device_data: Optional[SerialDevice] = None
        self.setupUi(self)
        self.done_button.clicked.connect(self.save_to_db)

    def open_save_data_window(self, db, serial_device: SerialDevice = None, **kwargs):
        SaveDialogWindow.db = db
        if serial_device is not None:
            self.device_data = serial_device
            self.device_name_input.setText(self.device_data.product_name)
        else:
            self.db_id = int(kwargs["id"])
            self.product_name = kwargs["product_name"]
            self.baud_rate = kwargs["baud_rate"]
            self.parity = kwargs["parity"]
            self.data_bits = kwargs["data_bits"]
            self.port_name = kwargs["port_name"]

            name = self.product_name.split('[')[0]
            self.device_name_input.setText(name.rstrip())
        self.exec()

    def save_to_db(self):
        device_name_input = self.device_name_input.text()

        if SaveDialogWindow.db is not None:
            if self.device_data is not None:
                if not self.port_check_box.isChecked():
                    self.device_data.port_name = "-"
                    self.device_data.port = "-"
                if device_name_input != self.device_data.product_name:
                    self.device_data.device_name = device_name_input
                else:
                    self.device_data.device_name = self.device_data.product_name
                SaveDialogWindow.db.insert_data(self.device_data)
            else:
                if device_name_input != self.product_name:
                    device_name = device_name_input
                else:
                    device_name = self.product_name

                if not self.port_check_box.isChecked():
                    self.port_name = "-"

                SaveDialogWindow.db.update_data(device_name, self.product_name, self.baud_rate, self.parity,
                                                self.data_bits, port_name=self.port_name, id=self.db_id)

        self.close()

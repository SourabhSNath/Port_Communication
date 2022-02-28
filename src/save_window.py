from typing import Optional

from PyQt6 import QtWidgets

from gui import save_window_ui
from src.data.serial_device import SerialDevice


# Dialog window that handles save operations.
class SaveDialogWindow(QtWidgets.QDialog, save_window_ui.Ui_Dialog):
    db = None

    def __init__(self):
        super(SaveDialogWindow, self).__init__()
        self.device_data: Optional[SerialDevice] = None
        self.setupUi(self)
        self.done_button.clicked.connect(self.save_to_db)

    def open_save_data_window(self, db, serial_device: SerialDevice):
        SaveDialogWindow.db = db
        self.device_data = serial_device
        self.device_name_input.setText(self.device_data.product_name)
        self.exec()

    def save_to_db(self):
        device_name_input = self.device_name_input.text()
        if not self.port_check_box.isChecked():
            self.device_data.port_name = "-"
            self.device_data.port = "-"

        if device_name_input != self.device_data.product_name:
            self.device_data.device_name = device_name_input
        else:
            self.device_data.device_name = self.device_data.product_name

        if SaveDialogWindow.db is not None:
            SaveDialogWindow.db.insert_data(self.device_data)
            print("Done")
            self.close()

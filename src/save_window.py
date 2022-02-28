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

    # def open_save_data_window(self, db, serial_device, **kwargs):
    #     SaveDialogWindow.db = db
    #     print(kwargs)
    #     self.device_name_input.setText(kwargs["product_name"])
    #     SaveDialogWindow.data = kwargs
    #     print("Save", SaveDialogWindow.data)
    #     self.exec()

    def open_save_data_window(self, db, serial_device: SerialDevice):
        SaveDialogWindow.db = db
        self.device_data = serial_device
        self.device_name_input.setText(self.device_data.product_name)
        print("Save", self.device_data)
        self.exec()

    def save_to_db(self):
        device_name_input = self.device_name_input.text()
        if not self.port_check_box.isChecked():
            self.device_data.port_name = "-"

        if device_name_input != self.device_data.product_name:
            self.device_data.device_name = device_name_input
        else:
            self.device_data.device_name = self.device_data.product_name

            if SaveDialogWindow.db is not None:
                SaveDialogWindow.db.insert_data(self.device_data)

    # def save_to_db(self):
    #     device = self.device_name_input.text()
    #     if self.port_check_box.isChecked():
    #         port_name = SaveDialogWindow.data["port_name"]
    #     else:
    #         port_name = "-"
    #     if device != SaveDialogWindow.data["product_name"]:
    #         device_name = device
    #     else:
    #         device_name = SaveDialogWindow.data["product_name"]
    #
    #     p_in = SaveDialogWindow.data["parity"]
    #
    #     # Quickly coded. Should probably be replaced with enums.
    #     if p_in == "No Parity":
    #         parity = 'N'
    #     elif p_in == "Odd":
    #         parity = 'O'
    #     else:
    #         parity = 'E'
    #
    #     if SaveDialogWindow.db is not None:
    #         SaveDialogWindow.db.insert_data(
    #             device_name=device_name, product_name=SaveDialogWindow.data["product_name"],
    #             serial_number=SaveDialogWindow.data["serial_number"],
    #             baud_rate=SaveDialogWindow.data["baud_rate"],
    #             parity_bits=parity,
    #             data_bits=SaveDialogWindow.data["data_bits"],
    #             port_name=port_name)
    #
    #     print("Done")
    #
    #     self.close()

from PyQt6 import QtWidgets

from gui import save_window_ui


class SaveDialogWindow(QtWidgets.QDialog, save_window_ui.Ui_Dialog):
    data = {}
    db = None

    def __init__(self):
        super(SaveDialogWindow, self).__init__()
        # self.db = DeviceDatabase()
        self.device_data = []
        print(self.device_data)
        self.setupUi(self)
        self.done_button.clicked.connect(self.save_to_db)

    def open_save_data_window(self, db, **kwargs):
        SaveDialogWindow.db = db
        print(kwargs)
        self.device_name_input.setText(kwargs["product_name"])
        SaveDialogWindow.data = kwargs
        print("Save", SaveDialogWindow.data)
        self.exec()

    def save_to_db(self):
        device = self.device_name_input.text()
        if self.port_check_box.isChecked():
            port_name = SaveDialogWindow.data["port_name"]
        else:
            port_name = "-"
        if device != SaveDialogWindow.data["product_name"]:
            device_name = device
        else:
            device_name = SaveDialogWindow.data["product_name"]

        p_in = SaveDialogWindow.data["parity"]
        if p_in == "No Parity":
            parity = 'N'
        elif p_in == "Odd":
            parity = 'O'
        else:
            parity = 'E'

        if SaveDialogWindow.db is not None:
            SaveDialogWindow.db.insert_data(
                device_name=device_name, product_name=SaveDialogWindow.data["product_name"],
                serial_number=SaveDialogWindow.data["serial_number"],
                baud_rate=SaveDialogWindow.data["baud_rate"],
                parity_bits=parity,
                data_bits=SaveDialogWindow.data["data_bits"],
                port_name=port_name)

        print("Done")

        self.close()

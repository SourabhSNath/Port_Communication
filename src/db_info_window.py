import os

from PyQt6 import QtWidgets

from src.Constants import DB_CREDENTIALS_FILE
from src.utils.file_operations import export_data_to_json, file_exists, import_data_from_json
from src.gui.db_info_window_ui import Ui_Dialog


class DatabaseInfoWindow(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, database=None):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.database = database
        self.db_info = None
        self.connect_button.clicked.connect(self.add_data_and_connect)
        if file_exists(DB_CREDENTIALS_FILE):
            self.load_db_info()
        else:
            self.current_database_box.deleteLater()
            self.gridLayout.removeItem(self.current_database_box)
            self.clear_item(self.current_database_box)
            self.current_use_label.setText("Please enter the credentials to access the database server.")

    def open_window(self, db):
        print("Shown")
        self.database = db
        self.show()
        self.exec()

    def add_data_and_connect(self):
        if self.connect_button.text() == "Connect":
            host = self.host_input.text().strip()
            user = self.user_input.text().strip()
            password = self.password_input.text().strip()
            database = self.db_name_input.text().strip()

            if host and user and password:
                db_info = {"host": host, "user": user, "password": password}
                if database:
                    db_info["database"] = database

                try:
                    self.database.connect_to_db(host=db_info["host"], user=db_info["user"],
                                                password=db_info["password"])

                    # Write new data
                    if file_exists(DB_CREDENTIALS_FILE):
                        os.remove(DB_CREDENTIALS_FILE)  # Delete previous file.
                    export_data_to_json(DB_CREDENTIALS_FILE, db_info)
                    self.load_db_info()
                    self.connect_button.setText("Disconnect")
                except Exception as e:
                    self.message_box(message=str(e))

            else:
                msg = QtWidgets.QMessageBox()
                msg.setText("Please Enter The Required Fields.")
                msg.setWindowTitle("Error")
                msg.exec()
        else:
            self.connect_button.setText("Connect")
            self.database.close_database_connection()

    def load_db_info(self):
        data = import_data_from_json(DB_CREDENTIALS_FILE)
        self.current_host_name.setText(data["host"])
        self.current_user_name.setText(data["user"])
        if "database" not in data:
            db_name = "serial_device_db"
        else:
            db_name = data["database"]
        self.current_database_name.setText(db_name)
        self.current_password_name.setText(data["password"])

    # Function to remove all the items within an item. Here used to remove everything within current_database_box.
    # https://stackoverflow.com/a/71070287/4273056
    def clear_item(self, item):
        layout = None
        if hasattr(item, "layout"):
            if callable(item.layout):
                layout = item.layout()

        widget = None
        if hasattr(item, "widget"):
            if callable(item.widget):
                widget = item.widget()

        if widget:
            widget.setParent(None)
        elif layout:
            for i in reversed(range(layout.count())):
                self.clear_item(layout.itemAt(i))

    @staticmethod
    def message_box(message):
        msg = QtWidgets.QMessageBox()
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec()

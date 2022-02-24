# Form implementation generated from reading ui file 'ui_files/main_communication_gui.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(993, 666)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.baud_rate_box = QtWidgets.QHBoxLayout()
        self.baud_rate_box.setContentsMargins(-1, -1, 8, -1)
        self.baud_rate_box.setObjectName("baud_rate_box")
        self.baud_rate_label = QtWidgets.QLabel(self.centralwidget)
        self.baud_rate_label.setMinimumSize(QtCore.QSize(72, 0))
        self.baud_rate_label.setMaximumSize(QtCore.QSize(72, 16777215))
        self.baud_rate_label.setObjectName("baud_rate_label")
        self.baud_rate_box.addWidget(self.baud_rate_label)
        self.baud_rate_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.baud_rate_combo_box.setMinimumSize(QtCore.QSize(150, 0))
        self.baud_rate_combo_box.setObjectName("baud_rate_combo_box")
        self.baud_rate_combo_box.addItem("")
        self.baud_rate_box.addWidget(self.baud_rate_combo_box)
        self.gridLayout.addLayout(self.baud_rate_box, 4, 0, 1, 3)
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setObjectName("connect_button")
        self.gridLayout.addWidget(self.connect_button, 6, 4, 1, 1)
        self.serial_number_box = QtWidgets.QFormLayout()
        self.serial_number_box.setObjectName("serial_number_box")
        self.serial_no_label = QtWidgets.QLabel(self.centralwidget)
        self.serial_no_label.setObjectName("serial_no_label")
        self.serial_number_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.serial_no_label)
        self.serial_no_input = QtWidgets.QLineEdit(self.centralwidget)
        self.serial_no_input.setObjectName("serial_no_input")
        self.serial_number_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.serial_no_input)
        self.gridLayout.addLayout(self.serial_number_box, 3, 3, 1, 2)
        self.device_name_box = QtWidgets.QFormLayout()
        self.device_name_box.setObjectName("device_name_box")
        self.device_label = QtWidgets.QLabel(self.centralwidget)
        self.device_label.setMinimumSize(QtCore.QSize(72, 0))
        self.device_label.setMaximumSize(QtCore.QSize(72, 16777215))
        self.device_label.setObjectName("device_label")
        self.device_name_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.device_label)
        self.device_combox_box = QtWidgets.QComboBox(self.centralwidget)
        self.device_combox_box.setObjectName("device_combox_box")
        self.device_name_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.device_combox_box)
        self.gridLayout.addLayout(self.device_name_box, 2, 0, 1, 5)
        self.port_name_box = QtWidgets.QFormLayout()
        self.port_name_box.setContentsMargins(-1, -1, 8, -1)
        self.port_name_box.setObjectName("port_name_box")
        self.port_label = QtWidgets.QLabel(self.centralwidget)
        self.port_label.setMinimumSize(QtCore.QSize(72, 0))
        self.port_label.setMaximumSize(QtCore.QSize(72, 16777215))
        self.port_label.setObjectName("port_label")
        self.port_name_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.port_label)
        self.port_input = QtWidgets.QLineEdit(self.centralwidget)
        self.port_input.setObjectName("port_input")
        self.port_name_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.port_input)
        self.gridLayout.addLayout(self.port_name_box, 3, 0, 1, 3)
        self.data_bit_box = QtWidgets.QHBoxLayout()
        self.data_bit_box.setContentsMargins(-1, -1, 0, -1)
        self.data_bit_box.setObjectName("data_bit_box")
        self.data_bit_label = QtWidgets.QLabel(self.centralwidget)
        self.data_bit_label.setMinimumSize(QtCore.QSize(0, 0))
        self.data_bit_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.data_bit_label.setObjectName("data_bit_label")
        self.data_bit_box.addWidget(self.data_bit_label)
        self.data_bit_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.data_bit_combobox.setMinimumSize(QtCore.QSize(60, 0))
        self.data_bit_combobox.setMaximumSize(QtCore.QSize(60, 16777215))
        self.data_bit_combobox.setObjectName("data_bit_combobox")
        self.data_bit_combobox.addItem("")
        self.data_bit_combobox.addItem("")
        self.data_bit_combobox.addItem("")
        self.data_bit_box.addWidget(self.data_bit_combobox)
        self.gridLayout.addLayout(self.data_bit_box, 4, 4, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.message_ox = QtWidgets.QVBoxLayout()
        self.message_ox.setContentsMargins(-1, -1, 8, -1)
        self.message_ox.setObjectName("message_ox")
        self.recieved_label = QtWidgets.QLabel(self.centralwidget)
        self.recieved_label.setObjectName("recieved_label")
        self.message_ox.addWidget(self.recieved_label)
        self.recieved_message_text_output = QtWidgets.QTextEdit(self.centralwidget)
        self.recieved_message_text_output.setObjectName("recieved_message_text_output")
        self.message_ox.addWidget(self.recieved_message_text_output)
        self.send_message_box = QtWidgets.QHBoxLayout()
        self.send_message_box.setContentsMargins(-1, 8, -1, -1)
        self.send_message_box.setObjectName("send_message_box")
        self.send_message_input = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_message_input.sizePolicy().hasHeightForWidth())
        self.send_message_input.setSizePolicy(sizePolicy)
        self.send_message_input.setMinimumSize(QtCore.QSize(0, 120))
        self.send_message_input.setMaximumSize(QtCore.QSize(16777215, 120))
        self.send_message_input.setObjectName("send_message_input")
        self.send_message_box.addWidget(self.send_message_input)
        self.send_message_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_message_button.setObjectName("send_message_button")
        self.send_message_box.addWidget(self.send_message_button)
        self.message_ox.addLayout(self.send_message_box)
        self.horizontalLayout_2.addLayout(self.message_ox)
        self.save_table_box = QtWidgets.QVBoxLayout()
        self.save_table_box.setObjectName("save_table_box")
        self.saved_label = QtWidgets.QLabel(self.centralwidget)
        self.saved_label.setObjectName("saved_label")
        self.save_table_box.addWidget(self.saved_label, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.saved_table = QtWidgets.QTableWidget(self.centralwidget)
        self.saved_table.setObjectName("saved_table")
        self.saved_table.setColumnCount(0)
        self.saved_table.setRowCount(0)
        self.save_table_box.addWidget(self.saved_table)
        self.horizontalLayout_2.addLayout(self.save_table_box)
        self.horizontalLayout_2.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 9, 0, 1, 5)
        spacerItem = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem1, 8, 4, 1, 1)
        self.save_to_database_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_to_database_button.setObjectName("save_to_database_button")
        self.gridLayout.addWidget(self.save_to_database_button, 7, 4, 1, 1)
        self.parity_bit_box = QtWidgets.QHBoxLayout()
        self.parity_bit_box.setContentsMargins(-1, -1, 8, -1)
        self.parity_bit_box.setObjectName("parity_bit_box")
        self.parity_label = QtWidgets.QLabel(self.centralwidget)
        self.parity_label.setMinimumSize(QtCore.QSize(0, 0))
        self.parity_label.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.parity_label.setObjectName("parity_label")
        self.parity_bit_box.addWidget(self.parity_label)
        self.parity_combobox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parity_combobox.sizePolicy().hasHeightForWidth())
        self.parity_combobox.setSizePolicy(sizePolicy)
        self.parity_combobox.setMinimumSize(QtCore.QSize(100, 0))
        self.parity_combobox.setObjectName("parity_combobox")
        self.parity_combobox.addItem("")
        self.parity_combobox.addItem("")
        self.parity_combobox.addItem("")
        self.parity_bit_box.addWidget(self.parity_combobox)
        self.gridLayout.addLayout(self.parity_bit_box, 4, 3, 1, 1)
        self.search_device_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_device_button.setMinimumSize(QtCore.QSize(120, 0))
        self.search_device_button.setMaximumSize(QtCore.QSize(120, 16777215))
        self.search_device_button.setObjectName("search_device_button")
        self.gridLayout.addWidget(self.search_device_button, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem2, 5, 4, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDelete_Database = QtGui.QAction(MainWindow)
        self.actionDelete_Database.setObjectName("actionDelete_Database")
        self.actionDelete_Table = QtGui.QAction(MainWindow)
        self.actionDelete_Table.setObjectName("actionDelete_Table")
        self.menuFile.addAction(self.actionDelete_Database)
        self.menuFile.addAction(self.actionDelete_Table)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.baud_rate_label.setText(_translate("MainWindow", "Baud Rate"))
        self.baud_rate_combo_box.setItemText(0, _translate("MainWindow", "110"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.serial_no_label.setText(_translate("MainWindow", "Serial Number"))
        self.device_label.setText(_translate("MainWindow", "Device"))
        self.port_label.setText(_translate("MainWindow", "Port Name"))
        self.data_bit_label.setText(_translate("MainWindow", "Data Bits"))
        self.data_bit_combobox.setItemText(0, _translate("MainWindow", "8"))
        self.data_bit_combobox.setItemText(1, _translate("MainWindow", "9"))
        self.data_bit_combobox.setItemText(2, _translate("MainWindow", "10"))
        self.recieved_label.setText(_translate("MainWindow", "Recieved"))
        self.send_message_input.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.send_message_button.setText(_translate("MainWindow", "Send Message"))
        self.saved_label.setText(_translate("MainWindow", "Saved"))
        self.save_to_database_button.setText(_translate("MainWindow", "Save"))
        self.parity_label.setText(_translate("MainWindow", "Parity Bits"))
        self.parity_combobox.setItemText(0, _translate("MainWindow", "No Parity"))
        self.parity_combobox.setItemText(1, _translate("MainWindow", "Odd"))
        self.parity_combobox.setItemText(2, _translate("MainWindow", "Even"))
        self.search_device_button.setText(_translate("MainWindow", "Scan All Devices"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionDelete_Database.setText(_translate("MainWindow", "Delete Database"))
        self.actionDelete_Table.setText(_translate("MainWindow", "Delete Table"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

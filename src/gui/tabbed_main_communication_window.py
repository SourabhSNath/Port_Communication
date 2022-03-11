# Form implementation generated from reading ui file 'src/gui/ui_files/tabbed_main_communication_gui.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.serial_tab = QtWidgets.QWidget()
        self.serial_tab.setObjectName("serial_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.serial_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.search_device_button = QtWidgets.QPushButton(self.serial_tab)
        self.search_device_button.setMinimumSize(QtCore.QSize(120, 0))
        self.search_device_button.setMaximumSize(QtCore.QSize(120, 16777215))
        self.search_device_button.setObjectName("search_device_button")
        self.gridLayout.addWidget(self.search_device_button, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(117, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.device_name_box = QtWidgets.QFormLayout()
        self.device_name_box.setObjectName("device_name_box")
        self.device_label = QtWidgets.QLabel(self.serial_tab)
        self.device_label.setMinimumSize(QtCore.QSize(72, 0))
        self.device_label.setMaximumSize(QtCore.QSize(72, 16777215))
        self.device_label.setObjectName("device_label")
        self.device_name_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.device_label)
        self.device_combox_box = QtWidgets.QComboBox(self.serial_tab)
        self.device_combox_box.setEditable(False)
        self.device_combox_box.setCurrentText("")
        self.device_combox_box.setObjectName("device_combox_box")
        self.device_name_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.device_combox_box)
        self.gridLayout.addLayout(self.device_name_box, 2, 0, 1, 3)
        self.port_name_box = QtWidgets.QFormLayout()
        self.port_name_box.setContentsMargins(-1, -1, 8, -1)
        self.port_name_box.setObjectName("port_name_box")
        self.port_label = QtWidgets.QLabel(self.serial_tab)
        self.port_label.setMinimumSize(QtCore.QSize(72, 0))
        self.port_label.setMaximumSize(QtCore.QSize(72, 16777215))
        self.port_label.setObjectName("port_label")
        self.port_name_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.port_label)
        self.port_input = QtWidgets.QLineEdit(self.serial_tab)
        self.port_input.setObjectName("port_input")
        self.port_name_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.port_input)
        self.gridLayout.addLayout(self.port_name_box, 3, 0, 1, 1)
        self.serial_number_box = QtWidgets.QFormLayout()
        self.serial_number_box.setObjectName("serial_number_box")
        self.serial_no_label = QtWidgets.QLabel(self.serial_tab)
        self.serial_no_label.setObjectName("serial_no_label")
        self.serial_number_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.serial_no_label)
        self.serial_no_input = QtWidgets.QLineEdit(self.serial_tab)
        self.serial_no_input.setObjectName("serial_no_input")
        self.serial_number_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.serial_no_input)
        self.gridLayout.addLayout(self.serial_number_box, 3, 1, 1, 2)
        self.baud_rate_box = QtWidgets.QHBoxLayout()
        self.baud_rate_box.setContentsMargins(-1, -1, 8, -1)
        self.baud_rate_box.setObjectName("baud_rate_box")
        self.baud_rate_label = QtWidgets.QLabel(self.serial_tab)
        self.baud_rate_label.setMinimumSize(QtCore.QSize(72, 0))
        self.baud_rate_label.setMaximumSize(QtCore.QSize(72, 16777215))
        self.baud_rate_label.setObjectName("baud_rate_label")
        self.baud_rate_box.addWidget(self.baud_rate_label)
        self.baud_rate_combo_box = QtWidgets.QComboBox(self.serial_tab)
        self.baud_rate_combo_box.setMinimumSize(QtCore.QSize(150, 0))
        self.baud_rate_combo_box.setObjectName("baud_rate_combo_box")
        self.baud_rate_combo_box.addItem("")
        self.baud_rate_box.addWidget(self.baud_rate_combo_box)
        self.gridLayout.addLayout(self.baud_rate_box, 4, 0, 1, 1)
        self.parity_bit_box = QtWidgets.QHBoxLayout()
        self.parity_bit_box.setContentsMargins(-1, -1, 8, -1)
        self.parity_bit_box.setObjectName("parity_bit_box")
        self.parity_label = QtWidgets.QLabel(self.serial_tab)
        self.parity_label.setMinimumSize(QtCore.QSize(0, 0))
        self.parity_label.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.parity_label.setObjectName("parity_label")
        self.parity_bit_box.addWidget(self.parity_label)
        self.parity_combobox = QtWidgets.QComboBox(self.serial_tab)
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
        self.gridLayout.addLayout(self.parity_bit_box, 4, 1, 1, 1)
        self.data_bit_box = QtWidgets.QHBoxLayout()
        self.data_bit_box.setContentsMargins(-1, -1, 0, -1)
        self.data_bit_box.setObjectName("data_bit_box")
        self.data_bit_label = QtWidgets.QLabel(self.serial_tab)
        self.data_bit_label.setMinimumSize(QtCore.QSize(0, 0))
        self.data_bit_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.data_bit_label.setObjectName("data_bit_label")
        self.data_bit_box.addWidget(self.data_bit_label)
        self.data_bit_combobox = QtWidgets.QComboBox(self.serial_tab)
        self.data_bit_combobox.setMinimumSize(QtCore.QSize(60, 0))
        self.data_bit_combobox.setMaximumSize(QtCore.QSize(60, 16777215))
        self.data_bit_combobox.setObjectName("data_bit_combobox")
        self.data_bit_combobox.addItem("")
        self.data_bit_combobox.addItem("")
        self.data_bit_combobox.addItem("")
        self.data_bit_combobox.addItem("")
        self.data_bit_box.addWidget(self.data_bit_combobox)
        self.gridLayout.addLayout(self.data_bit_box, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(120, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.connect_button = QtWidgets.QPushButton(self.serial_tab)
        self.connect_button.setObjectName("connect_button")
        self.gridLayout.addWidget(self.connect_button, 6, 2, 1, 1)
        self.save_to_database_button = QtWidgets.QPushButton(self.serial_tab)
        self.save_to_database_button.setObjectName("save_to_database_button")
        self.gridLayout.addWidget(self.save_to_database_button, 7, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(120, 27, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem2, 8, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.message_ox = QtWidgets.QVBoxLayout()
        self.message_ox.setContentsMargins(-1, -1, 8, -1)
        self.message_ox.setObjectName("message_ox")
        self.recieved_label = QtWidgets.QLabel(self.serial_tab)
        self.recieved_label.setObjectName("recieved_label")
        self.message_ox.addWidget(self.recieved_label)
        self.recieved_message_text_output = QtWidgets.QTextEdit(self.serial_tab)
        self.recieved_message_text_output.setObjectName("recieved_message_text_output")
        self.message_ox.addWidget(self.recieved_message_text_output)
        self.send_message_box = QtWidgets.QHBoxLayout()
        self.send_message_box.setContentsMargins(-1, 8, -1, -1)
        self.send_message_box.setObjectName("send_message_box")
        self.send_message_input = QtWidgets.QTextEdit(self.serial_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_message_input.sizePolicy().hasHeightForWidth())
        self.send_message_input.setSizePolicy(sizePolicy)
        self.send_message_input.setMinimumSize(QtCore.QSize(0, 120))
        self.send_message_input.setMaximumSize(QtCore.QSize(16777215, 120))
        self.send_message_input.setObjectName("send_message_input")
        self.send_message_box.addWidget(self.send_message_input)
        self.send_message_button = QtWidgets.QPushButton(self.serial_tab)
        self.send_message_button.setObjectName("send_message_button")
        self.send_message_box.addWidget(self.send_message_button)
        self.message_ox.addLayout(self.send_message_box)
        self.horizontalLayout_2.addLayout(self.message_ox)
        self.save_table_box = QtWidgets.QVBoxLayout()
        self.save_table_box.setObjectName("save_table_box")
        self.saved_label = QtWidgets.QLabel(self.serial_tab)
        self.saved_label.setObjectName("saved_label")
        self.save_table_box.addWidget(self.saved_label, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.saved_table = QtWidgets.QTableWidget(self.serial_tab)
        self.saved_table.setObjectName("saved_table")
        self.saved_table.setColumnCount(0)
        self.saved_table.setRowCount(0)
        self.save_table_box.addWidget(self.saved_table)
        self.horizontalLayout_2.addLayout(self.save_table_box)
        self.horizontalLayout_2.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 9, 0, 1, 3)
        self.tabWidget.addTab(self.serial_tab, "")
        self.ethernet_tab = QtWidgets.QWidget()
        self.ethernet_tab.setObjectName("ethernet_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.ethernet_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.eth_search_device_button = QtWidgets.QPushButton(self.ethernet_tab)
        self.eth_search_device_button.setMinimumSize(QtCore.QSize(120, 0))
        self.eth_search_device_button.setMaximumSize(QtCore.QSize(120, 16777215))
        self.eth_search_device_button.setObjectName("eth_search_device_button")
        self.gridLayout_2.addWidget(self.eth_search_device_button, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(117, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        self.eth_device_name_box = QtWidgets.QFormLayout()
        self.eth_device_name_box.setObjectName("eth_device_name_box")
        self.eth_device_label = QtWidgets.QLabel(self.ethernet_tab)
        self.eth_device_label.setMinimumSize(QtCore.QSize(72, 0))
        self.eth_device_label.setMaximumSize(QtCore.QSize(72, 16777215))
        self.eth_device_label.setObjectName("eth_device_label")
        self.eth_device_name_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.eth_device_label)
        self.eth_device_combox_box = QtWidgets.QComboBox(self.ethernet_tab)
        self.eth_device_combox_box.setEditable(False)
        self.eth_device_combox_box.setCurrentText("")
        self.eth_device_combox_box.setObjectName("eth_device_combox_box")
        self.eth_device_name_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.eth_device_combox_box)
        self.gridLayout_2.addLayout(self.eth_device_name_box, 2, 0, 1, 3)
        self.eth_port_name_box = QtWidgets.QFormLayout()
        self.eth_port_name_box.setContentsMargins(-1, -1, 8, -1)
        self.eth_port_name_box.setObjectName("eth_port_name_box")
        self.eth_port_label = QtWidgets.QLabel(self.ethernet_tab)
        self.eth_port_label.setMinimumSize(QtCore.QSize(72, 0))
        self.eth_port_label.setMaximumSize(QtCore.QSize(72, 16777215))
        self.eth_port_label.setObjectName("eth_port_label")
        self.eth_port_name_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.eth_port_label)
        self.eth_port_input = QtWidgets.QLineEdit(self.ethernet_tab)
        self.eth_port_input.setObjectName("eth_port_input")
        self.eth_port_name_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.eth_port_input)
        self.gridLayout_2.addLayout(self.eth_port_name_box, 3, 0, 1, 1)
        self.eth_serial_number_box = QtWidgets.QFormLayout()
        self.eth_serial_number_box.setObjectName("eth_serial_number_box")
        self.eth_serial_no_label = QtWidgets.QLabel(self.ethernet_tab)
        self.eth_serial_no_label.setObjectName("eth_serial_no_label")
        self.eth_serial_number_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.eth_serial_no_label)
        self.eth_serial_no_input = QtWidgets.QLineEdit(self.ethernet_tab)
        self.eth_serial_no_input.setObjectName("eth_serial_no_input")
        self.eth_serial_number_box.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.eth_serial_no_input)
        self.gridLayout_2.addLayout(self.eth_serial_number_box, 3, 1, 1, 2)
        self.eth_baud_rate_box = QtWidgets.QHBoxLayout()
        self.eth_baud_rate_box.setContentsMargins(-1, -1, 8, -1)
        self.eth_baud_rate_box.setObjectName("eth_baud_rate_box")
        self.eth_baud_rate_label = QtWidgets.QLabel(self.ethernet_tab)
        self.eth_baud_rate_label.setMinimumSize(QtCore.QSize(72, 0))
        self.eth_baud_rate_label.setMaximumSize(QtCore.QSize(72, 16777215))
        self.eth_baud_rate_label.setObjectName("eth_baud_rate_label")
        self.eth_baud_rate_box.addWidget(self.eth_baud_rate_label)
        self.eth_baud_rate_combo_box = QtWidgets.QComboBox(self.ethernet_tab)
        self.eth_baud_rate_combo_box.setMinimumSize(QtCore.QSize(150, 0))
        self.eth_baud_rate_combo_box.setObjectName("eth_baud_rate_combo_box")
        self.eth_baud_rate_combo_box.addItem("")
        self.eth_baud_rate_box.addWidget(self.eth_baud_rate_combo_box)
        self.gridLayout_2.addLayout(self.eth_baud_rate_box, 4, 0, 1, 1)
        self.eth_parity_bit_box = QtWidgets.QHBoxLayout()
        self.eth_parity_bit_box.setContentsMargins(-1, -1, 8, -1)
        self.eth_parity_bit_box.setObjectName("eth_parity_bit_box")
        self.eth_parity_label = QtWidgets.QLabel(self.ethernet_tab)
        self.eth_parity_label.setMinimumSize(QtCore.QSize(0, 0))
        self.eth_parity_label.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.eth_parity_label.setObjectName("eth_parity_label")
        self.eth_parity_bit_box.addWidget(self.eth_parity_label)
        self.eth_parity_combobox = QtWidgets.QComboBox(self.ethernet_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eth_parity_combobox.sizePolicy().hasHeightForWidth())
        self.eth_parity_combobox.setSizePolicy(sizePolicy)
        self.eth_parity_combobox.setMinimumSize(QtCore.QSize(100, 0))
        self.eth_parity_combobox.setObjectName("eth_parity_combobox")
        self.eth_parity_combobox.addItem("")
        self.eth_parity_combobox.addItem("")
        self.eth_parity_combobox.addItem("")
        self.eth_parity_bit_box.addWidget(self.eth_parity_combobox)
        self.gridLayout_2.addLayout(self.eth_parity_bit_box, 4, 1, 1, 1)
        self.eth_data_bit_box = QtWidgets.QHBoxLayout()
        self.eth_data_bit_box.setContentsMargins(-1, -1, 0, -1)
        self.eth_data_bit_box.setObjectName("eth_data_bit_box")
        self.eth_data_bit_label = QtWidgets.QLabel(self.ethernet_tab)
        self.eth_data_bit_label.setMinimumSize(QtCore.QSize(0, 0))
        self.eth_data_bit_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.eth_data_bit_label.setObjectName("eth_data_bit_label")
        self.eth_data_bit_box.addWidget(self.eth_data_bit_label)
        self.eth_data_bit_combobox = QtWidgets.QComboBox(self.ethernet_tab)
        self.eth_data_bit_combobox.setMinimumSize(QtCore.QSize(60, 0))
        self.eth_data_bit_combobox.setMaximumSize(QtCore.QSize(60, 16777215))
        self.eth_data_bit_combobox.setObjectName("eth_data_bit_combobox")
        self.eth_data_bit_combobox.addItem("")
        self.eth_data_bit_combobox.addItem("")
        self.eth_data_bit_combobox.addItem("")
        self.eth_data_bit_combobox.addItem("")
        self.eth_data_bit_box.addWidget(self.eth_data_bit_combobox)
        self.gridLayout_2.addLayout(self.eth_data_bit_box, 4, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(120, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem4, 5, 2, 1, 1)
        self.eth_connect_button = QtWidgets.QPushButton(self.ethernet_tab)
        self.eth_connect_button.setObjectName("eth_connect_button")
        self.gridLayout_2.addWidget(self.eth_connect_button, 6, 2, 1, 1)
        self.eth_save_to_database_button = QtWidgets.QPushButton(self.ethernet_tab)
        self.eth_save_to_database_button.setObjectName("eth_save_to_database_button")
        self.gridLayout_2.addWidget(self.eth_save_to_database_button, 7, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(120, 27, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 8, 2, 1, 1)
        self.eth_horizontalLayout = QtWidgets.QHBoxLayout()
        self.eth_horizontalLayout.setObjectName("eth_horizontalLayout")
        self.eth_message_ox = QtWidgets.QVBoxLayout()
        self.eth_message_ox.setContentsMargins(-1, -1, 8, -1)
        self.eth_message_ox.setObjectName("eth_message_ox")
        self.eth_recieved_label = QtWidgets.QLabel(self.ethernet_tab)
        self.eth_recieved_label.setObjectName("eth_recieved_label")
        self.eth_message_ox.addWidget(self.eth_recieved_label)
        self.eth_recieved_message_text_output = QtWidgets.QTextEdit(self.ethernet_tab)
        self.eth_recieved_message_text_output.setObjectName("eth_recieved_message_text_output")
        self.eth_message_ox.addWidget(self.eth_recieved_message_text_output)
        self.eth_send_message_box = QtWidgets.QHBoxLayout()
        self.eth_send_message_box.setContentsMargins(-1, 8, -1, -1)
        self.eth_send_message_box.setObjectName("eth_send_message_box")
        self.eth_send_message_input = QtWidgets.QTextEdit(self.ethernet_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eth_send_message_input.sizePolicy().hasHeightForWidth())
        self.eth_send_message_input.setSizePolicy(sizePolicy)
        self.eth_send_message_input.setMinimumSize(QtCore.QSize(0, 120))
        self.eth_send_message_input.setMaximumSize(QtCore.QSize(16777215, 120))
        self.eth_send_message_input.setObjectName("eth_send_message_input")
        self.eth_send_message_box.addWidget(self.eth_send_message_input)
        self.eth_send_message_button = QtWidgets.QPushButton(self.ethernet_tab)
        self.eth_send_message_button.setObjectName("eth_send_message_button")
        self.eth_send_message_box.addWidget(self.eth_send_message_button)
        self.eth_message_ox.addLayout(self.eth_send_message_box)
        self.eth_horizontalLayout.addLayout(self.eth_message_ox)
        self.eth_save_table_box = QtWidgets.QVBoxLayout()
        self.eth_save_table_box.setObjectName("eth_save_table_box")
        self.eth_saved_label = QtWidgets.QLabel(self.ethernet_tab)
        self.eth_saved_label.setObjectName("eth_saved_label")
        self.eth_save_table_box.addWidget(self.eth_saved_label, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.eth_saved_table = QtWidgets.QTableWidget(self.ethernet_tab)
        self.eth_saved_table.setObjectName("eth_saved_table")
        self.eth_saved_table.setColumnCount(0)
        self.eth_saved_table.setRowCount(0)
        self.eth_save_table_box.addWidget(self.eth_saved_table)
        self.eth_horizontalLayout.addLayout(self.eth_save_table_box)
        self.eth_horizontalLayout.setStretch(1, 3)
        self.gridLayout_2.addLayout(self.eth_horizontalLayout, 9, 0, 1, 3)
        self.tabWidget.addTab(self.ethernet_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_export_data = QtGui.QAction(MainWindow)
        self.action_export_data.setObjectName("action_export_data")
        self.action_load_data = QtGui.QAction(MainWindow)
        self.action_load_data.setObjectName("action_load_data")
        self.action_delete_data = QtGui.QAction(MainWindow)
        self.action_delete_data.setObjectName("action_delete_data")
        self.action_database_credentials = QtGui.QAction(MainWindow)
        self.action_database_credentials.setObjectName("action_database_credentials")
        self.menuFile.addAction(self.action_export_data)
        self.menuFile.addAction(self.action_load_data)
        self.menuFile.addAction(self.action_delete_data)
        self.menuDatabase.addAction(self.action_database_credentials)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.device_combox_box.setCurrentIndex(-1)
        self.eth_device_combox_box.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_device_button.setText(_translate("MainWindow", "Scan All Devices"))
        self.device_label.setText(_translate("MainWindow", "Device"))
        self.port_label.setText(_translate("MainWindow", "Port Name"))
        self.serial_no_label.setText(_translate("MainWindow", "Serial Number"))
        self.baud_rate_label.setText(_translate("MainWindow", "Baud Rate"))
        self.baud_rate_combo_box.setItemText(0, _translate("MainWindow", "110"))
        self.parity_label.setText(_translate("MainWindow", "Parity Bits"))
        self.parity_combobox.setItemText(0, _translate("MainWindow", "No Parity"))
        self.parity_combobox.setItemText(1, _translate("MainWindow", "Odd"))
        self.parity_combobox.setItemText(2, _translate("MainWindow", "Even"))
        self.data_bit_label.setText(_translate("MainWindow", "Data Bits"))
        self.data_bit_combobox.setItemText(0, _translate("MainWindow", "5"))
        self.data_bit_combobox.setItemText(1, _translate("MainWindow", "6"))
        self.data_bit_combobox.setItemText(2, _translate("MainWindow", "7"))
        self.data_bit_combobox.setItemText(3, _translate("MainWindow", "8"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.save_to_database_button.setText(_translate("MainWindow", "Save"))
        self.recieved_label.setText(_translate("MainWindow", "Recieved"))
        self.send_message_input.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.send_message_button.setText(_translate("MainWindow", "Send Message"))
        self.saved_label.setText(_translate("MainWindow", "Saved"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.serial_tab), _translate("MainWindow", "Serial"))
        self.eth_search_device_button.setText(_translate("MainWindow", "Scan All Devices"))
        self.eth_device_label.setText(_translate("MainWindow", "Device"))
        self.eth_port_label.setText(_translate("MainWindow", "IP Address"))
        self.eth_serial_no_label.setText(_translate("MainWindow", "Port Name"))
        self.eth_baud_rate_label.setText(_translate("MainWindow", "Baud Rate"))
        self.eth_baud_rate_combo_box.setItemText(0, _translate("MainWindow", "110"))
        self.eth_parity_label.setText(_translate("MainWindow", "Parity Bits"))
        self.eth_parity_combobox.setItemText(0, _translate("MainWindow", "No Parity"))
        self.eth_parity_combobox.setItemText(1, _translate("MainWindow", "Odd"))
        self.eth_parity_combobox.setItemText(2, _translate("MainWindow", "Even"))
        self.eth_data_bit_label.setText(_translate("MainWindow", "Data Bits"))
        self.eth_data_bit_combobox.setItemText(0, _translate("MainWindow", "5"))
        self.eth_data_bit_combobox.setItemText(1, _translate("MainWindow", "6"))
        self.eth_data_bit_combobox.setItemText(2, _translate("MainWindow", "7"))
        self.eth_data_bit_combobox.setItemText(3, _translate("MainWindow", "8"))
        self.eth_connect_button.setText(_translate("MainWindow", "Connect"))
        self.eth_save_to_database_button.setText(_translate("MainWindow", "Save"))
        self.eth_recieved_label.setText(_translate("MainWindow", "Recieved"))
        self.eth_send_message_input.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.eth_send_message_button.setText(_translate("MainWindow", "Send Message"))
        self.eth_saved_label.setText(_translate("MainWindow", "Saved"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ethernet_tab), _translate("MainWindow", "Ethernet"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.action_export_data.setText(_translate("MainWindow", "Export Data"))
        self.action_load_data.setText(_translate("MainWindow", "Load Data"))
        self.action_delete_data.setText(_translate("MainWindow", "Delete All Data"))
        self.action_database_credentials.setText(_translate("MainWindow", "Database Login Credentials"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

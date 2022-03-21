from typing import Optional

from PyQt6.QtCore import pyqtSignal, QDir, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QWidget, QStatusBar
from loguru import logger

from src.gui.ethernet_tab import Ui_Ethernet_Widget
from src.main.tcp_client import TcpClient
from src.main.tcp_server import TcpServer


class EthernetTab(QWidget, Ui_Ethernet_Widget):
    submitted = pyqtSignal(str)
    server_signal = pyqtSignal(TcpServer, str)

    def __init__(self, parent=None, statusbar: QStatusBar = None):
        super(EthernetTab, self).__init__(parent)
        self.setupUi(self)
        self.setup_baud_rate()
        port_reg_expr = "^[0-9]*$"
        ports_validator = QRegularExpressionValidator(QRegularExpression(port_reg_expr))
        self.server_port_no_input.setValidator(ports_validator)
        self.recipient_port_no_input.setValidator(ports_validator)

        self.statusbar = statusbar

        self.server_port = None
        self.client_add = None
        self.client_port = None

        self.connect_eth_button.clicked.connect(self.connect)
        self.eth_send_button.clicked.connect(self.send_message)

        self.server: Optional[TcpServer] = None
        self.client: Optional[TcpClient] = None
        self.is_server = False

    def connect(self):
        if self.connect_eth_button.text() == "Connect":
            if port := self.server_port_no_input.text().strip():
                self.server = TcpServer()
                print(self.server)
                self.server.received.connect(self.write_msg)
                print("Start Server", port)
                self.server_start_listening(int(port))
                self.connect_eth_button.setText("Disconnect")
                self.is_server = True
            elif (ad := self.client_recipient_address_input.text()) \
                    and (port := self.recipient_port_no_input.text()):
                self.client_add = ad
                self.client_port = int(port.strip())
                print("Connect Client", ad, port)
                self.client = TcpClient()
                self.client.sent.connect(self.write_msg)
                self.client.received.connect(self.write_client_msg)
                self.client_connection(ad, int(port))
                self.connect_eth_button.setText("Disconnect")
                self.is_server = False
            else:
                print("Please enter client or server information.")
        else:
            try:
                if self.is_server:
                    print("Closing server")
                    self.server.close()
                else:
                    print("Closing client")
                    self.client.close()
                self.connect_eth_button.setText("Connect")
            except Exception as e:
                logger.error(f"Can't close connection:\n {e}")

    def server_start_listening(self, port):
        if port:
            print("Starting..")
            self.server.listen_for_connection(int(port))
        else:
            print("Please enter the port number")

    def client_connection(self, recipient, port):
        print("Client connection")
        is_connected = self.client.create_connection(recipient, port)
        if is_connected:
            self.statusbar.showMessage("Connected")
        else:
            self.statusbar.showMessage("Connection Failed. Try Again.")
            print("Couldn't connect to server.")

    def send_message(self):
        username = QDir.home().dirName()
        msg = self.eth_send_message_input.toPlainText()

        baud_rate = self.eth_baud_rate_combo_box.currentText()
        parity = self.eth_parity_combobox.currentText()
        data_bits = self.eth_data_bit_combobox.currentText()

        if self.server is not None:
            print(f"Server sending on port: {self.server_port}")
            self.server.send_msg(user=username, msg=msg, baud_rate=baud_rate, parity=parity, data_bits=data_bits)
        elif self.client is not None:
            print(f"Client sending to address: {self.client_add} on port: {self.client_port}")
            self.client.send_msg(username, msg, self.client_add, self.client_port)
        else:
            print("Client/Server not setup")

    def write_msg(self, user, msg):
        print("Show message.", user, msg)
        self.eth_recieved_message_text_output.append(f"{user}: {msg}")

    def write_client_msg(self, user, msg, baud_rate, parity, data_bits):
        self.eth_recieved_message_text_output.append(f"{user}: {msg}\n"
                                                     f"{baud_rate = }, {parity = }, {data_bits = }")

    # Set Baud rates programmatically since the numbers aren't known.
    def setup_baud_rate(self):
        baud_rates = [110, 150, 300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600]
        self.eth_baud_rate_combo_box.clear()  # Clearing the default 110 set in the ui file inorder to prevent 2 copies.
        for rate in baud_rates:
            self.eth_baud_rate_combo_box.addItem(str(rate))

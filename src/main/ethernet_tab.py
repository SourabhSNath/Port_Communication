from PyQt6.QtCore import pyqtSignal, QDir
from PyQt6.QtNetwork import QTcpSocket
from PyQt6.QtWidgets import QWidget, QStatusBar

from src.gui.ethernet_tab import Ui_Ethernet_Widget
from src.network.tcp_controller import TcpController


class EthernetTab(QWidget, Ui_Ethernet_Widget):
    submitted = pyqtSignal(str)

    def __init__(self, parent=None, statusbar: QStatusBar = None):
        super(EthernetTab, self).__init__(parent)
        self.setupUi(self)

        self.statusbar = statusbar
        self.tcp_socket = QTcpSocket(self)

        self.tcp_controller: TcpController = TcpController()

        self.connect_eth_button.clicked.connect(self.start_listening)
        self.eth_send_button.clicked.connect(self.send_msg)

        self.tcp_controller.received.connect(self.write_msg)

    def start_listening(self):
        port = self.eth_port_no_input.text().strip()
        if port:
            print("Starting..")
            self.tcp_controller.listen_for_connection(int(port))
        else:
            print("Please enter the port number")

    # TODO: NOTE: Recipient is required for both server and client.
    #  Since TCP needs to know both the sides.
    def send_msg(self):
        username = QDir.home().dirName()
        recipient = self.eth_address_input.text().strip()
        port = self.recipient_port_no_input.text()
        if self.tcp_controller is not None:
            msg = self.eth_send_message_input.toPlainText()
            print(msg)
            self.tcp_controller.send_msg(user=username, recipient=recipient, msg=msg, port=port)
        else:
            print("No tcp controller")

    def write_msg(self, msg_len, user, msg):
        print("Writing in tab", msg_len, user, msg)
        self.eth_recieved_message_text_output.append(f"{user}: {msg}")

# ---------------------------
# # (?:...) is to say that it is a non capturing group, | is or, so it allows ',' or ', ' or '-'
# ports_reg_exp = "[0-9]+((?:,|, |-)[0-9]+)+"
# ports_validator = QRegularExpressionValidator(QRegularExpression(ports_reg_exp))
# self.eth_port_no_input.setValidator(ports_validator)

# def scan_ports(self):
#     port_in = self.eth_port_no_input.text().rstrip()
#     if port_in.endswith(",") or port_in.endswith("-"):
#         port_in = port_in[:-1]
#
#     if "-" in port_in and (", " in port_in or "," in port_in):
#         print(", and - present together in string, error")
#     else:
#         # Example: 19-80 port i.e 19 to 80
#         if '-' in port_in:
#             start, end = port_in.split("-")
#             ports = [p for p in range(int(start), int(end) + 1)]
#             print(ports)
#         else:
#             # This is a list of ports
#             ports = [int(port.strip()) for port in port_in.split(',')]
#             print(ports)
#         ipaddress = self.eth_address_input.text()
#         # self.tcp_socket.connectToHost(address=ipaddress, port=port_in)
#
#         # print(ports)

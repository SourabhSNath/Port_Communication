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
        self.server_add = None
        self.server_port = None
        self.client_add = None
        self.client_port = None

        print("Getting Peer IP", self.tcp_controller.get_peer_ip())

        self.connect_eth_button.clicked.connect(self.connect)
        self.eth_send_button.clicked.connect(self.send_msg)

        self.tcp_controller.received.connect(self.write_msg)

    def connect(self):
        if self.connect_eth_button.text() == "Connect":
            if (port := self.server_port_no_input.text().strip()) and \
                    (add := self.server_recipient_address_input.text()):
                self.server_port = port
                self.server_add = add
                self.server_start_listening(port)
            elif (ad := self.client_recipient_address_input).text() \
                    and (port := self.recipient_port_no_input.text()):
                self.client_add = ad
                self.client_port = port.strip()
                self.client_connection(ad, port)
            else:
                print("Please enter client or server information.")
        else:
            self.tcp_controller.stop_connection()

    def server_start_listening(self, port):
        if port:
            print("Starting..")
            self.tcp_controller.listen_for_connection(int(port))
        else:
            print("Please enter the port number")

    def client_connection(self, recipient, port):
        is_connected = self.tcp_controller.client_create_connection(recipient, int(port))

        if is_connected:
            self.statusbar.showMessage("Connected")
            print("Connected to client/server")
        else:
            self.statusbar.showMessage("Connection Failed. Try Again.")
            print("Client/Server Connection Failed")

    # TODO: NOTE: Recipient is required for both server and client.
    #  Since TCP needs to know both the sides.
    def send_msg(self):
        username = QDir.home().dirName()
        # add = self.server_recipient_address_input.text()
        # port = self.server_port_no_input.text()
        if self.client_port and self.client_add:
            add = self.client_add
            port = self.client_port
        else:
            add = self.server_add
            port = self.server_port

        if self.tcp_controller is not None:
            msg = self.eth_send_message_input.toPlainText()
            print(msg)
            if add and port:
                self.tcp_controller.send_msg(user=username, msg=msg, recipient_address=add, port=int(port))
            else:
                print("Sending without add and port")
                self.tcp_controller.send_msg(user=username, msg=msg)
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

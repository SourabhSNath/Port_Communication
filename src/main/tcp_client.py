from PyQt6 import QtNetwork, QtCore
from PyQt6.QtCore import pyqtSignal
from loguru import logger


class TcpClient(QtNetwork.QTcpSocket):
    # received = pyqtSignal(str, str)
    received = pyqtSignal(str, str, int, str, int)
    sent = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()

        self.errorOccurred.connect(self.on_error)
        self.is_client_connected = False

    def on_error(self, socket_error):
        logger.error(socket_error)

    # Pass a slot here, so that the readyRead will trigger the slot.
    def connection(self):
        print("Setting readyRead")
        self.readyRead.connect(self.data_received)

    def data_received(self):
        print("Data Received")
        datastream = QtCore.QDataStream(self)
        if not self.bytesAvailable():
            pass
        else:
            print("Received data has bytes")
            # Doing this in order of information being sent
            username = datastream.readQString()
            raw_msg = datastream.readQString()

            baud_rate = datastream.readInt()
            parity = datastream.readQString()
            data_bits = datastream.readInt()

            print(f"{username =}, {raw_msg =}, {baud_rate =}, {parity =}, {data_bits =}")

            if raw_msg and username:
                print("Received:", username, raw_msg)
                # self.received.emit(username, raw_msg)
                self.received.emit(username, raw_msg, baud_rate, parity, data_bits)

    def create_connection(self, recipient_address: str, port: int):
        print("Attempting to connect to server.")

        socket_state = self.state()
        # Check if the socket isn't connected a remote host
        if socket_state != QtNetwork.QAbstractSocket.SocketState.ConnectedState:
            # Then connect
            print(f"Connecting since not in Connected State to {recipient_address} on port {port}")
            self.connectToHost(
                recipient_address, port
            )
            self.connection()

            self.is_client_connected = (self.state() == QtNetwork.QTcpSocket.SocketState.ConnectedState)
            print("Is client connected", self.is_client_connected)
            return self.is_client_connected
        else:
            print("Already connected to Server")
            return self.is_client_connected

    def send_msg(self, user, msg, recipient_address: str, port: int):

        if recipient_address is not None and port is not None:
            self.create_connection(recipient_address, port)

        datastream = QtCore.QDataStream(self)

        datastream.writeQString(user)
        datastream.writeQString(msg)
        print(f"Sending to {port =}: ", user, msg)

        # self.received.emit(user, msg)
        self.sent.emit(user, msg)

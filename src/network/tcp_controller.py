from PyQt6 import QtNetwork, QtCore
from PyQt6.QtCore import QObject, pyqtSignal
from loguru import logger


class TcpController(QObject):
    received = pyqtSignal(int, str, str)
    error = pyqtSignal(str)

    # For checking the data to see if the data is corrupted.
    message_length = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self.port = None

        self.server = QtNetwork.QTcpServer()
        # self.server.listen(QtNetwork.QHostAddress.SpecialAddress.Any, self.port)

        self.server.acceptError.connect(self.on_error)

        # Emitted whenever a new connection comes into the server
        self.server.newConnection.connect(self.on_connection)
        self.connections = []

        self.client_socket = QtNetwork.QTcpSocket()
        self.client_socket.errorOccurred.connect(self.on_error)

    def listen_for_connection(self, port):
        # The dual stack any-address. A socket bound with this address will listen on both IPv4 and IPv6 interfaces.
        # if the port is 0, the port gets chosen automatically
        self.port = port
        self.server.listen(QtNetwork.QHostAddress.SpecialAddress.Any, port)

    def on_error(self, socket_error):
        logger.error(socket_error)

    def on_connection(self):
        # Next Waiting connection, returns QTcpSocket object
        connection = self.server.nextPendingConnection()
        connection.readyRead.connect(self.process_datastream)
        self.connections.append(connection)

    def process_datastream(self):
        for socket in self.connections:
            datastream = QtCore.QDataStream(socket)

            if not socket.bytesAvailable():
                continue
            else:
                # Doing this in order of information being sent
                msg_length = datastream.readUInt32()
                if self.message_length == msg_length:
                    username = datastream.readQString()
                    print(msg_length)
                    raw_msg = datastream.readQString()

                    if raw_msg and username:
                        self.received.emit(username, raw_msg)

    def send_msg(self, user, recipient, msg, port):
        socket_state = self.client_socket.state()

        # Check if the socket isn't connected a remote host
        if socket_state != QtNetwork.QAbstractSocket.SocketState.ConnectedState:
            # Then connect
            print("Connecting since not in Connected State")
            self.client_socket.connectToHost(
                recipient, int(port) if port else self.port
            )

        datastream = QtCore.QDataStream(self.client_socket)

        length = len(msg)
        self.message_length.emit(length)  # TODO MOVE BELOW WRITING
        datastream.writeUInt32(length)
        datastream.writeQString(user)
        datastream.writeQString(msg)
        print("Sending: ", length, user, msg)

        self.received.emit(length, user, msg)

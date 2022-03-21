from PyQt6 import QtNetwork, QtCore
from PyQt6.QtCore import pyqtSignal
from loguru import logger


class TcpServer(QtNetwork.QTcpServer):
    received = pyqtSignal(str, str)
    # received = pyqtSignal(str, str, int, str, int)
    error = pyqtSignal(str)

    def __init__(self):
        super(TcpServer, self).__init__()
        self.port = None

        self.acceptError.connect(self.on_error)

        self.newConnection.connect(self.on_connection)
        self.connections = []

        self.is_listening = False
        self.is_client_connected = False

    def listen_for_connection(self, port):
        # The dual stack any-address. A socket bound with this address will listen on both IPv4 and IPv6 interfaces.
        # if the port is 0, the port gets chosen automatically
        self.port = port
        self.is_listening = self.listen(QtNetwork.QHostAddress.SpecialAddress.Any, port)
        print("Is Server Listening:", self.is_listening)

    def on_error(self, err):
        logger.error(err)

    def on_connection(self):
        # Next Waiting connection, returns QTcpSocket object
        connection = self.nextPendingConnection()
        connection.readyRead.connect(self.process_datastream)
        self.connections.append(connection)

    def process_datastream(self):
        for socket in self.connections:
            print("Socket Info", socket.peerName(), socket.peerPort(), socket.peerAddress())
            datastream = QtCore.QDataStream(socket)

            if not socket.bytesAvailable():
                continue
            else:
                print("Received data has bytes")
                # Doing this in order of information being sent
                # msg_length = datastream.readUInt32()

                username = datastream.readQString()
                # print(msg_length)
                raw_msg = datastream.readQString()

                if raw_msg and username:
                    print("Received:", username, raw_msg)
                    self.received.emit(username, raw_msg)

    def send_msg(self, user, msg, baud_rate, parity, data_bits):
        print("Server mode")
        for socket in self.connections:
            print("Sending to Socket Info", socket.peerName(), socket.peerPort(), socket.peerAddress())

            datastream = QtCore.QDataStream(socket)
            datastream.writeQString(user)
            datastream.writeQString(msg)
            datastream.writeInt(int(baud_rate))
            datastream.writeQString(parity)
            datastream.writeInt(int(data_bits))
            self.received.emit(user, msg)

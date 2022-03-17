from PyQt6 import QtNetwork, QtCore
from PyQt6.QtCore import QObject, pyqtSignal, QByteArray
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
        self.server.acceptError.connect(self.on_error)

        # Emitted whenever a new connection comes into the server
        self.server.newConnection.connect(self.on_connection)
        self.connections = []

        self.is_listening = False
        self.is_client_connected = False

        self.client_socket = QtNetwork.QTcpSocket()
        self.client_socket.errorOccurred.connect(self.on_error)

    def listen_for_connection(self, port):
        # The dual stack any-address. A socket bound with this address will listen on both IPv4 and IPv6 interfaces.
        # if the port is 0, the port gets chosen automatically
        self.port = port
        self.is_listening = self.server.listen(QtNetwork.QHostAddress.SpecialAddress.Any, port)
        print("Is Server listening:", self.is_listening)

    def on_error(self, socket_error):
        logger.error(socket_error)

    def on_connection(self):
        # Next Waiting connection, returns QTcpSocket object
        connection = self.server.nextPendingConnection()
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
                msg_length = datastream.readUInt32()

                username = datastream.readQString()
                print(msg_length)
                raw_msg = datastream.readQString()

                if raw_msg and username:
                    print("Received:", username, raw_msg)
                    self.received.emit(msg_length, username, raw_msg)

                    print(f"{msg_length = }")

    def client_create_connection(self, recipient_address: str, port: int):
        print("Attempting to connect to the other ip.")
        socket_state = self.client_socket.state()

        # Check if the socket isn't connected a remote host
        if socket_state != QtNetwork.QAbstractSocket.SocketState.ConnectedState:
            # Then connect
            print(f"Connecting since not in Connected State to {recipient_address} on port {port}")
            self.client_socket.connectToHost(
                recipient_address, port
            )

            self.is_client_connected = self.client_socket.waitForConnected(2000)
            print("Is client connected", self.is_client_connected)
            return self.is_client_connected
        else:
            print("Already connected to Server/ Client")
            return self.is_client_connected

    def send_msg(self, user, msg, recipient_address: str = None, port: int = None):

        if not self.is_listening:

            if recipient_address is not None and port is not None:
                self.client_create_connection(recipient_address, port)

            datastream = QtCore.QDataStream(self.client_socket)

            length = len(msg)
            self.message_length.emit(length)
            datastream.writeUInt32(length)
            datastream.writeQString(user)
            datastream.writeQString(msg)
            print(f"Sending to {port =}: ", length, user, msg)

            self.received.emit(length, user, msg)
        else:
            print("Server mode")
            for socket in self.connections:
                print("Sending to Socket Info", socket.peerName(), socket.peerPort(), socket.peerAddress())
                socket.write(msg.encode("utf-8"))

                # if s.socketDescriptor() == socketId:
                #     message = "You> {}".format(text)
                # else:
                #     message = "{}> {}".format(socketId, text)
                # reply = QByteArray()
                # stream = QDataStream(reply, QIODevice.WriteOnly)
                # stream.setVersion(QDataStream.Qt_4_2)
                # stream.writeUInt32(0)
                # stream.writeQString(message)
                # stream.device().seek(0)
                # stream.writeUInt32(reply.size() - SIZEOF_UINT32)
                # s.write(reply)


    def get_peer_ip(self):
        return self.client_socket.peerAddress().toString()

    def stop_connection(self):
        self.server.close()

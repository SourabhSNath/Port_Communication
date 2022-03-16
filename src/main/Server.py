from PyQt6 import QtNetwork
from PyQt6.QtCore import pyqtSignal


class Server(QtNetwork.QTcpServer):
    clientConnected = pyqtSignal()
    clientDisconnected = pyqtSignal()

    received = pyqtSignal(str, str)
    error = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.connections = []
        self.newConnection.connect(self.on_connection)

    def create_connection(self, port):
        is_connected = self.listen(QtNetwork.QHostAddress.SpecialAddress.Any, port)
        self.acceptError.connect(self.on_error)
        return is_connected

    def on_connection(self):
        # Next Waiting connection, returns QTcpSocket object
        connection = self.nextPendingConnection()
        connection.readyRead.connect(self.process_datastream)
        self.connections.append(connection)



from PyQt6 import QtWidgets, QtNetwork, QtCore
from PyQt6.QtCore import pyqtSignal, QObject


class ChatWindow(QtWidgets.QWidget):
    submitted = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QGridLayout())
        self.checkbox = QtWidgets.QCheckBox("Use UDP")
        self.layout().addWidget(self.checkbox, 1, 2)
        self.msg_view = QtWidgets.QTextEdit()
        self.msg_view.setReadOnly(True)
        self.layout().addWidget(self.msg_view, 2, 1, 1, 2)
        self.msg_entry = QtWidgets.QLineEdit()
        self.layout().addWidget(self.msg_entry, 3, 1)
        self.send_btn = QtWidgets.QPushButton("Send")
        self.layout().addWidget(self.send_btn, 3, 2)

        self.send_btn.clicked.connect(self.send_msg)

    def write_msg(self, username, msg):
        self.msg_view.append(f'<b>{username}: </b> {msg} <br>')

    def send_msg(self):
        msg = self.msg_entry.text().strip()
        if msg:
            self.submitted.emit(msg)
            self.msg_entry.clear()


# UDP is certainly simple to work with, but it has many limitations. For example, UDP
# broadcasts cannot usually be routed outside a local network, and the lack of stateful
# connection means that there is no way to know whether a transmission was
# received or lost.
class UdpChatInterface(QObject):
    port = 7777
    delimiter = '||'  # Simply to separate username and msg
    received = pyqtSignal(str, str)
    error = pyqtSignal(str)

    def __init__(self, username):
        super().__init__()
        self.username = username

        # After calling super() and storing the username variable, our first order of business is
        # to create and configure a QUdpSocket object. Before we can use the socket,
        # it must be bound to a localhost address and a port number.
        #
        # QtNetwork.QHostAddress.SpecialAddress.Any
        # represents all addresses on the local system so our socket will be listening and
        # sending on port 7777 on all local interfaces.
        self.socket = QtNetwork.QUdpSocket()
        self.socket.bind(QtNetwork.QHostAddress.SpecialAddress.Any, self.port)

        self.socket.readyRead.connect(self.process_datagrams)
        self.socket.errorOccurred.connect(self.on_error)

    def on_error(self, socket_error):
        print(socket_error)

        # OLD METHOD. Doesnt work anymore. socket_error is directly the error instead in PyQt6
        #
        # Network errors are defined in the
        # SocketError enum of the QAbstractSocket class (the parent class of UdpSocket).
        # Unfortunately, if we just try to print the error, we get the integer value of the
        # constant.
        # To actually get a meaningful string, we're going to dig into the
        # staticMetaObject associated with QAbstractSocket. We first get the index of the enum
        # class containing the error constants, then use valueToKey() to convert our socket
        # error integer into its constant name.
        #
        # This trick can be used with any Qt enum to retrieve a meaningful name rather than just its integer value.
        # One that's been retrieved, we simply format the error in a message and emit it in
        # our error signal.
        # error_index = QtNetwork.QAbstractSocket.staticMetaObject.indexOfEnumerator('SocketError')
        #
        # error = QtNetwork.QAbstractSocket.staticMetaObject \
        #     .enumerator(error_index).valueToKey(socket_error)
        # message = f"There was a network error: {error}"
        # self.error.emit(message)

    # A single UDP transmission is known as a datagram.
    def process_datagrams(self):
        while self.socket.hasPendingDatagrams():
            # we loop continually while there are pending datagrams, calling the socket's
            # receiveDatagram() method, which returns and removes the next datagram waiting in
            # the buffer until all the datagrams are retrieved.
            datagram = self.socket.receiveDatagram()
            raw_msg = bytes(datagram.data()).decode("utf-8")

            # we need to CHECK it to make sure it came from
            # ANOTHER INSTANCE of udp_chat.py, then split it out into its username and message
            # components:
            if self.delimiter not in raw_msg:
                continue
            username, message = raw_msg.split(self.delimiter, 1)
            self.received.emit(username, message)

    def send_msg(self, msg):
        msg_bytes = f'{self.username}{self.delimiter}{msg}'.encode("utf-8")
        # Destination is specified as QHostAddress.Broadcast,
        # which indicates that we want to use the broadcast address
        # The broadcast address is a reserved address on a TCP/IP network which, when used,
        # indicates that the transmission should be received by all hosts.
        self.socket.writeDatagram(msg_bytes, QtNetwork.QHostAddress.SpecialAddress.Broadcast, self.port)


# TCP is a stateful transmission protocol, meaning that a connection is established
# and maintained until the transmission is complete. TCP is also primarily a one-to
# one connection between hosts, which we generally implement using a client-server
# design.
class TCPChatInterface(QObject):
    port = 7777
    delimeter = '||'
    received = pyqtSignal(str, str)
    error = pyqtSignal(str)

    # Since TCP Requires direct connection to another host, recipient argument is required.
    def __init__(self, username, recipient):
        super().__init__()
        self.username = username
        self.recipient = recipient

        self.server = QtNetwork.QTcpServer()
        self.server.listen(QtNetwork.QHostAddress.SpecialAddress.Any, self.port)
        self.server.acceptError.connect(self.on_error)

        # The newConnection signal is emitted whenever a new connection comes into the
        # server
        self.server.newConnection.connect(self.on_connection)
        self.connections = []

        self.client_socket = QtNetwork.QTcpSocket()
        self.client_socket.errorOccurred.connect(self.on_error)

    def on_connection(self):
        connection = self.server.nextPendingConnection()  # Next waiting connection, returns QTcpSocket object
        connection.readyRead.connect(self.process_datastream)
        self.connections.append(connection)

    def process_datastream(self):
        # A socket is a file-like object that represents a single point of network connectivity for
        # the system. Every socket has a host address, network port, and transmission protocol.

        # We're iterating through the connected sockets and passing each to a QDataStream
        # object. The socket object has a bytesAvailable() method that tells us how many
        # bytes of data are queued up to be read.
        # If this number is zero, we're going to continue to the next connection in the list.
        for socket in self.connections:
            self.datastream = QtCore.QDataStream(socket)
            if not socket.bytesAvailable():
                continue
            else:
                # Doing this according to the order at which data was sent.
                msg_length = self.datastream.readUInt32()
                print(msg_length)
                raw_msg = self.datastream.readQString()

                if raw_msg and self.delimeter in raw_msg:
                    username, msg = raw_msg.split(self.delimeter, 1)
                    self.received.emit(username, msg)

    def send_msg(self, msg):
        raw_msg = f"{self.username}{self.delimeter}{msg}"

        socket_state = self.client_socket.state()
        # Check if the socket is not connected to a remote host
        if socket_state != QtNetwork.QAbstractSocket.SocketState.ConnectedState:
            # Connect
            self.client_socket.connectToHost(
                self.recipient, self.port
            )

        self.datastream = QtCore.QDataStream(self.client_socket)

        # The objects can be pulled from the datastream only in the order we send them.
        # So prefixing the string with the length so the recipient can check for corruption.
        self.datastream.writeUInt32(len(raw_msg))
        self.datastream.writeQString(raw_msg)

        # Emit the msg locally so that the local display can show it.
        # Since this isn't a broadcast message, our local TCP Server wont hear the message being sent out.
        self.received.emit(self.username, msg)

    def on_error(self, socket_error):
        # Magic to get the enum name

        print(socket_error)
        # try:
        #     error_index = (QtNetwork.QAbstractSocket
        #                    .staticMetaObject
        #                    .indexOfEnumerator('SocketError'))
        #     error = (QtNetwork.QAbstractSocket
        #              .staticMetaObject
        #              .enumerator(error_index)
        #              .valueToKey(socket_error))
        #     message = f"There was a network error: {error}"
        #     self.error.emit(message)
        # except Exception as e:
        #     print(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    username = QtCore.QDir.home().dirName()

    chat = ChatWindow()

    recipient, _ = QtWidgets.QInputDialog.getText(
        None, "Recipient", "Specify the IP or hostname of the remote host"
    )
    if not recipient:
        sys.exit()

    interface = TCPChatInterface(username, recipient)
    chat.submitted.connect(interface.send_msg)
    interface.received.connect(chat.write_msg)
    interface.error.connect(
        lambda x: QtWidgets.QMessageBox.critical(None, 'Error', x)
    )

    # interface = UdpChatInterface(username)
    #
    # chat.submitted.connect(interface.send_msg)
    # interface.received.connect(chat.write_msg)
    # interface.error.connect(
    #     lambda x: QtWidgets.QMessageBox.critical(None, 'Error', x)
    # )

    chat.show()
    app.exec()

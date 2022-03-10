from PyQt6 import QtSerialPort, QtCore
from PyQt6.QtCore import pyqtSignal
from loguru import logger

from src.data.model.serial_device import SerialDevice

"""
    Class to handle device communication related codes. Entire class could be reworked for better performance.
"""


class DataSignal(QtCore.QObject):
    read_message_signal = pyqtSignal(str)


class SerialCommunication(QtCore.QObject):
    received_data = pyqtSignal(str)
    received_data_list = []

    def __init__(self):
        super().__init__()
        self.data_signal = DataSignal()
        self._port_list = None
        self.eol = '\r'.encode()  # Carriage Return
        self.buffer = QtCore.QByteArray()
        self.serial = QtSerialPort.QSerialPort()
        self.serial.readyRead.connect(self.read_data)

    @logger.catch()
    def get_all_devices(self):
        ports = QtSerialPort.QSerialPortInfo.availablePorts()

        def serial_device(device):
            return SerialDevice(product_name=device.description(), port_name=device.portName(),
                                port=device.systemLocation(),
                                serial_number=device.serialNumber())

        self.port_list = [serial_device(device) for device in ports]
        print(self.port_list)
        return self.port_list

    @logger.catch()
    def connection(self, port_location, baud_rate, parity, data_bit, device):
        if not self.serial.isOpen():
            print("From Serial Com", port_location)
            self.serial.setPort(QtSerialPort.QSerialPortInfo(port_location))
            self.serial.setBaudRate(int(baud_rate))
            print(SerialDevice.get_parity_with_index(index=parity))
            print(QtSerialPort.QSerialPort.DataBits.Data8)
            self.serial.setParity(SerialDevice.get_parity_with_index(index=parity))
            # self.serial.setParity(parity)
            # self.serial.setDataBits(data_bit)
            result = self.serial.open(QtCore.QIODevice.OpenModeFlag.ReadWrite)
            print(f"Connection Result for {device}: {result}")
            return result

    # TODO: Check with actual serial device. canReadLine doesn't work with these devices, manually attaching '\r'
    #  to separate the end points. Comparative codes are different and bigger, doesn't work with these devices.
    @QtCore.pyqtSlot()
    def read_data(self):
        print("read_data fun")
        data = self.serial.readAll()
        print(data)
        self.buffer.append(data)
        if self.buffer.contains(b'\r'):
            print("EOL")
            try:
                # data = self.buffer.trimmed().data().decode()
                print("using datastream")

                stream = QtCore.QDataStream(self.buffer)
                data = stream.readBytes()
                self.data_signal.read_message_signal.emit(data.decode())
                self.buffer.clear()
            except Exception as e:
                logger.error("Error while reading: {}", e)
        else:
            print("NO EOL")

        # while self.serial.canReadLine():
        #     data = self.serial.readLine()
        #     print(data)

    def write_data(self, message: str):
        print(f"Writing {message}")
        # self.serial.write(message.encode())
        stream = QtCore.QDataStream(self.serial)
        stream.writeBytes(message.encode())

    @property
    def port_list(self):
        return self._port_list if not None else []

    @port_list.setter
    def port_list(self, value):
        self._port_list = value

    def get_connection_status(self):
        return self.serial.isOpen()

    def close_connection(self):
        self.serial.close()


# ----------------------------------------------------------------
"""
    def __init__(self):
        self.port_list = []
        self.serial_connection = None
        self.continuous_read = False

    def get_all_devices(self):
        ports = serial.tools.list_ports.comports()
        for p in sorted(ports):
            # https://pyserial.readthedocs.io/en/latest/tools.html
            # Don't know the difference between interface and product, since both are being reported as the same here.
            self.port_list.append(
                SerialDevice(product_name=p.product, port_name=p.name, port=p.device, serial_number=p.serial_number,
                             ))
        #     interface=p.interface
        print(self.port_list)
        return self.port_list

    # For connecting to the device.
    def connection(self, port_location, baud_rate, parity, data_bit):
        if parity == "No Parity":
            p_in = serial.Serial.PARITIES[0]
        elif parity == "Odd":
            p_in = serial.Serial.PARITIES[2]
        else:
            p_in = serial.Serial.PARITIES[1]

        try:
            self.serial_connection = serial.Serial(port_location, baudrate=baud_rate, timeout=1, parity=p_in,
                                                   bytesize=data_bit)
            print(self.serial_connection, type(self.serial_connection))
        except Exception as e:
            print(f"Exception {e}")

    def read_data(self):
        if self.serial_connection is not None:
            SerialCommunication.received_data_list.clear()
            while True:
                received_data = self.serial_connection.readline()
                if received_data:
                    SerialCommunication.received_data_list.append(received_data.rstrip())
                    print("Received", received_data)
                else:
                    break

    def write_data(self, msg):
        if msg == "read":
            self.continuous_read = True
        else:
            self.continuous_read = False

        if self.serial_connection is not None and self.serial_connection.isOpen():
            print("Inside write data", f"{self.serial_connection.port}", self.serial_connection.isOpen())
            self.serial_connection.write(msg.encode())
            self.read_data()

    def get_connection_status(self):
        return self.serial_connection.isOpen()

    def close_connection(self):
        if self.serial_connection.isOpen():
            self.serial_connection.close()
        return self.serial_connection.isOpen()
"""

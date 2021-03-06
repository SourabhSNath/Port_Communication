import dataclasses
from PyQt6.QtSerialPort import QSerialPort

"""
Model Object that represents the data for the serial device.
"""


class Parity:
    NO_PARITY = QSerialPort.Parity.NoParity
    ODD = QSerialPort.Parity.OddParity
    EVEN = QSerialPort.Parity.EvenParity


class DataBit:
    FIVE = QSerialPort.DataBits.Data5
    SIX = QSerialPort.DataBits.Data6
    SEVEN = QSerialPort.DataBits.Data7
    EIGHT = QSerialPort.DataBits.Data8


@dataclasses.dataclass
class SerialDevice:
    product_name: str
    port_name: str  # Port name like tty or com
    port: str  # port location like /dev/ttyUSB0
    serial_number: str
    # interface: str

    # User input data
    device_name: str = None
    baud_rate: int = None
    data_bits: int = None
    parity: Parity = Parity.NO_PARITY

    def get_parity_string(self):
        if self.parity == Parity.NO_PARITY:
            return "NO Parity"
        elif self.parity == Parity.EVEN:
            return "Even"
        else:
            return "Odd"

    @staticmethod
    def get_parity_with_index(index):
        match index:
            case 0:
                return Parity.NO_PARITY
            case 1:
                return Parity.ODD
            case 2:
                return Parity.EVEN

    def __repr__(self):
        if self.device_name is None:
            return f"""
            Device(
                    Product Name: {self.product_name},
                    Port Name: {self.port_name},
                    Port: {self.port},
                    Serial Number: {self.serial_number}
                )
        """
        # Interface: {self.interface}
        else:
            return f"""
                Device(
                        Device Name: {self.device_name},
                        Product Name: {self.product_name}
                        Port Name: {self.port_name},
                        Port: {self.port},
                        Serial Number: {self.serial_number},
                        Baud Rate: {self.baud_rate},
                        Parity: {self.parity},
                        Data Bits: {self.data_bits}
                    )
                """

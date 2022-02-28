import dataclasses

from enum import Enum
from typing import Optional


class Parity(Enum):
    NO_PARITY = 'N'
    ODD = 'O'
    EVEN = 'E'


class SerialDevice:

    def __init__(self, product_name, port_name, port, serial_number, interface, device_name: str = None,
                 baud_rate: int = 0,
                 data_bits: int = 0, parity=Parity.NO_PARITY):
        self.product_name = product_name
        self.port_name = port_name
        self.port = port
        self.serial_number = serial_number
        self.interface = interface
        self.device_name: str = device_name
        self._baud_rate: int = baud_rate
        self.data_bits: int = data_bits
        self.parity: Parity = parity

    @property
    def baud_rate(self):
        return self._baud_rate

    @baud_rate.setter
    def baud_rate(self, value):
        self._baud_rate = value

    def __repr__(self):
        if self.device_name is None:
            return f"""
            Device(
                    Product Name: {self.product_name},
                    Port Name: {self.port_name},
                    Port: {self.port},
                    Serial Number: {self.serial_number},
                    Interface: {self.interface}
                )
        """
        else:
            return f"""
                Device(
                        Device Name: {self.device_name},
                        Product Name: {self.product_name}
                        Port Name: {self.port_name},
                        Port: {self.port},
                        Serial Number: {self.serial_number},
                        Interface: {self.interface},
                        Device Name: {self.device_name},
                        Baud Rate: {self.baud_rate},
                        Parity: {self.parity},
                        Data Bits: {self.data_bits}
                    )
                """

#
# @dataclasses.dataclass
# class SerialDevice:
#     product_name: str
#     # Port name like tty or com
#     port_name: str
#     # port location like /dev/ttyUSB0
#     port: str
#     serial_number: str
#     interface: str
#
#     # User input data
#     device_name: str
#     baud_rate: int
#     data_bits: int
#     parity: Parity = Parity.NO_PARITY
#
#
#
# def __repr__(self):
#     if self.device_name is None:
#         return f"""
#         Device(
#                 Product Name: {self.product_name},
#                 Port Name: {self.port_name},
#                 Port: {self.port},
#                 Serial Number: {self.serial_number},
#                 Interface: {self.interface}
#             )
#     """
#     else:
#         return f"""
#             Device(
#                     Device Name: {self.device_name},
#                     Product Name: {self.product_name}
#                     Port Name: {self.port_name},
#                     Port: {self.port},
#                     Serial Number: {self.serial_number},
#                     Interface: {self.interface},
#                     Device Name: {self.device_name},
#                     Baud Rate: {self.baud_rate},
#                     Parity: {self.parity},
#                     Data Bits: {self.data_bits}
#                 )
#             """

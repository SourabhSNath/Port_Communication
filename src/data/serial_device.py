import dataclasses

"""
Model Object that represents the data for the serial device.
"""


class Parity:
    NO_PARITY = 'N'
    ODD = 'O'
    EVEN = 'E'


@dataclasses.dataclass
class SerialDevice:
    product_name: str
    port_name: str  # Port name like tty or com
    port: str  # port location like /dev/ttyUSB0
    serial_number: str
    interface: str

    # User input data
    device_name: str = None
    baud_rate: int = None
    data_bits: int = None
    parity: Parity = Parity.NO_PARITY

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

import serial.tools.list_ports

from src.data.serial_device import SerialDevice


# Class to handle device communication related codes. Entire class could be reworked for better performance.
class SerialCommunication:
    received_data = ""
    received_data_list = []

    def __init__(self):
        self.port_list = []
        self.serial_connection = None
        self.is_connected = False

    def get_all_devices(self):
        ports = serial.tools.list_ports.comports()
        for p in sorted(ports):
            # https://pyserial.readthedocs.io/en/latest/tools.html
            # Don't know the difference between interface and product, since both are being reported as the same here.
            self.port_list.append(
                SerialDevice(product_name=p.product, port_name=p.name, port=p.device, serial_number=p.serial_number,
                             interface=p.interface))
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
            self.is_connected = self.serial_connection.isOpen()
            print(self.serial_connection, type(self.serial_connection))
        except Exception as e:
            self.is_connected = False
            print(f"Exception {e}")

    def read_data(self):
        if self.serial_connection is not None and self.is_connected:
            SerialCommunication.received_data_list.clear()
            while True:
                received_data = self.serial_connection.readline()
                if received_data:
                    SerialCommunication.received_data_list.append(received_data.rstrip())
                    print("Received", received_data)
                else:
                    break

    def write_data(self, msg):
        if self.serial_connection is not None and self.is_connected:
            print("Inside write data", f"{self.serial_connection.port}", self.is_connected)
            self.serial_connection.write(msg.encode())
            self.read_data()

    def get_connection_status(self):
        return self.is_connected

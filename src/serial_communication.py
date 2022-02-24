import serial.tools.list_ports


class SerialCommunication:
    received_data = ""

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
                {"Port Name": p.name, "Port": p.device, "Serial Number": p.serial_number, "Interface": p.interface,
                 "Device": p.product})
        print(self.port_list)
        return self.port_list

    def connection(self, port_location, baud_rate):
        try:
            self.serial_connection = serial.Serial(port_location, baudrate=baud_rate, timeout=1)
            self.is_connected = self.serial_connection.is_open
            print(self.serial_connection, type(self.serial_connection))
        except Exception as e:
            self.is_connected = False
            print(f"Exception {e}")

    def read_data(self):
        if self.serial_connection is not None and self.is_connected:
            SerialCommunication.received_data = self.serial_connection.readline()
            print(SerialCommunication.received_data)

    def write_data(self, msg):
        if self.serial_connection is not None and self.is_connected:
            print("Inside write data", f"{self.serial_connection.port}", self.is_connected)
            self.serial_connection.write(msg.encode())
            self.read_data()

    def get_connection_status(self):
        return self.is_connected

import serial.tools.list_ports


def get_all_devices():
    port_list = []
    ports = serial.tools.list_ports.comports()
    for p in sorted(ports):
        # https://pyserial.readthedocs.io/en/latest/tools.html
        # Don't know the difference between interface and product, since both are being reported as the same here.
        port_list.append(
            {"PortName": p.name, "Port": p.device, "Serial Number": p.serial_number, "interface": p.interface,
             "device": p.product})
    print(port_list)
    return port_list


get_all_devices()

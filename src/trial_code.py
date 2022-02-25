from time import sleep

import serial.tools.list_ports

# Basic python code for testing device.
ports = serial.tools.list_ports.comports()
port_list = []
for p in sorted(ports):
    port_list.append({"Port": p.device, "Serial Number": p.serial_number, "interface": p.interface})
print(port_list)

ser = serial.Serial(port_list[0]["Port"], timeout=1, baudrate=119000)
msg = "Hi"
# Encode required for turning the string to byte array
ser.write(msg.encode())
# Adding sleep to wait for the reply since the reply may not arrive sometimes otherwise
sleep(0.5)
l = ser.readline()
print(l)

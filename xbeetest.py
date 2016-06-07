import serial
from xbee import XBee

com_port = "/dev/tty.usbserial-DN01DSAC"
baudrate = 115200


ser = serial.Serial(com_port, baudrate)
xbee = XBee(ser)

while True:
	try:
		print xbee.wait_read_frame()
	except KeyboardInterrupt:
		break
ser.close()
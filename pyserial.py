import serial

# Establish serial communication (Example: COM3, Baud rate 9600)
ser = serial.Serial('COM3', 9600)

# Read data from machine
data = ser.readline().decode('utf-8').strip()
print("Received Data:", data)

ser.close()

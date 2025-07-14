import serial

ser = serial.Serial("COM3", 115200)  # Replace COM3 with your port!

print("Listening for pedal signal...")

while True:
    if ser.in_waiting:
        line = ser.readline().decode().strip()
        print(f"Message from board: {line}")

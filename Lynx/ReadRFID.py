import serial
### Import Serial Module
ser=serial.Serial('COM13',9600)
## COM1 With Baud 9600
data=ser.read(12)
if data=="26008B2938BC":
  print "Access Granted"
elif data=="4B009929F00B":
  print "Access Denied"
else:
  print "Car Stolen"

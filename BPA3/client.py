import socket

SERVICE_CENTER = ("100.65.156.79", 8000)
print(SERVICE_CENTER) 

eyecar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
eyecar.connect(SERVICE_CENTER)  #connect to the server port
print("Connected to", SERVICE_CENTER)

#1
eyecar.send('arrival_service|'.encode())

msg = ''
while True:
    symbol = eyecar.recv(1).decode()
    if symbol in ('|', ''): break
    msg += symbol    

print(msg)

#2
eyecar.send('equipment_destroy|'.encode())

msg = ''
while True:
    symbol = eyecar.recv(1).decode()
    if symbol in ('|', ''): break
    msg += symbol    

print(msg)

#3
eyecar.send('install_needed_equipment|'.encode())

msg = ''
while True:
    symbol = eyecar.recv(1).decode()
    if symbol in ('|', ''): break
    msg += symbol    

print(msg)

#4
eyecar.send('left_service|'.encode())

msg = ''
while True:
    symbol = eyecar.recv(1).decode()
    if symbol in ('|', ''): break
    msg += symbol    

print(msg)




#for 1 client

import socket

SERVICE_CENTER = ("100.65.156.79", 8000)
print(SERVICE_CENTER)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVICE_CENTER) 
server.listen()   #listen to the server port

print("I am listening your connections")

client, address = server.accept()

while True:
    msg = ''
    while True:
        symbol = client.recv(1).decode()
        if symbol in ('|', ''): break
        msg += symbol
    
    print(msg)
    if msg == "arrival_service": 
        client.send(str("its_clear|").encode())
    
    elif msg == "equipment_destroy":
        client.sendall('unloading_has_begun|'.encode())
         
    elif msg == "install_needed_equipment":
        client.sendall('in_progress|'.encode())

    elif msg == "left_service":
        client.sendall('goodbye|'.encode())

         
            
        
    
    # elif msg.startswith('hub,give'):  
    #     if current_equipment == equipments[0]: #'no_equipment'
    #         eq_id = int(msg.split(',')[-1])
    #         current_equipment = equipments[eq_id] 
    #         client.sendall('ok|'.encode())
    #     else:
    #         client.sendall('error|'.encode())
    #         fail = True
            
    
    # elif msg == 'equip_ready':
    #     sock.close()
    #     if current_equipment == need_equipment and reserved_task == nearest_task_id and not fail:
    #         return True
    #     else:
    #         return False
    
    else:
        server.close()
        break
        

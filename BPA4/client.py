import socket



POINTS = [(1, 0.15, 1.8, 0.4), 
          (1, 0.6, 1.8, 0.85),
          (0.1, 0.8, 0.3, 1.6),
           (0.7, 0.75, 1, 1.55),
            (2.15, 0.75,	2.6, 1.55),
            (0.1, 3, 0.3, 3.6),
            (0.7, 3,	1, 3.75),
            (1.9, 3.2, 2.3, 3.7),
            (1, 4.1, 1.5, 4.4),
            (1.15, 4.2, 1.8, 4.5)
          ]

MOVE ={
    1:"left, right"  ,
    2:"forward, left",
    3:"forward, left" ,
    4:"left, right",
    5: "forward, left, left",
    6: "right, left" ,
    7:   "forward, right" ,
    8:  "forward, right, right" ,
    9:  "forward, right" ,
    10:  "right, left" 
}

points = []
min_id_zone = 1

ZONE1 = [2, 3, 7, 10]
ZONE2 = [1, 4, 6, 9]
ZONE3 = [5, 8]
ZONES = [ZONE1, ZONE2, ZONE3]

SERVICE_CENTER = ("172.16.65.91", 5000)

eyecar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
eyecar.connect(SERVICE_CENTER)  #connect to the server port
print("Connected to", SERVICE_CENTER)

eyecar.send('hello'.encode())

msg = ''
while True:
    symbol = eyecar.recv(1).decode()
    if symbol in ('|', ''): break
    msg += symbol
print(msg)


msg_list = msg.split(";")
msg_list.pop()

#print(msg_list)

for task_x_y in msg_list:
    task, x, y =  task_x_y.split(":")
    print(task)

for task_x_y in msg_list:
    task, x, y =  task_x_y.split(":")
    


    for id, point in enumerate(POINTS):
        #print(point)
        if (point[0] <= float(x) <= point[2]) and (point[1] <= float(y) <= point[3]):
            pts = id +1
           # print("точка",pts) #номер точки
            for z, cur in enumerate(ZONES):
                if pts in cur:
                    id_zone = z+1
                    #print("id_zone",id_zone)

                    if id_zone == 1:
                        print("Ближайшее",task)
                        exit()
                        
                    if id_zone == 2:
                        #print("task",task)
                        
                        main_task = task

                    elif id_zone == 3:
                        #print("task",task)
                        continue
    
            break


print("Ближайшее",main_task)
move = MOVE.get(pts)
print(move)
eyecar.close()
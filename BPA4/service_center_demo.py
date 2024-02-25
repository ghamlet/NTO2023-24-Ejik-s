"""
Ответ от Сервисного Центра приходит в следующем формате:
...;situationN:xN:yN;
(x, y) - координаты происшествия
situation - один из типов происшествия ('fire', 'injury', 'pipes', 'vehicles')
"""
from random import choice, randint, shuffle, uniform
import socket


p1 = (1, 0.15, 1.8, 0.4)
p2 = (1, 0.6, 1.8, 0.85)
p3 = (0.1, 0.8, 0.3, 1.6)
p4 = (0.7, 0.75, 1, 1.55)
p5 = (2.15, 0.75,	2.6, 1.55)
p6 = (0.1, 3, 0.3, 3.6)
p7 = (0.7, 3,	1, 3.75)    
p8 = (1.9, 3.2, 2.3, 3.7)
p9 = (1, 4.1, 1.5, 4.4)
p10 = (1.15, 4.2, 1.8, 4.5)

# Координаты зон
ZONE1 = [p2, p3, p7, p10]
ZONE2 = [p1, p4, p6, p9]
ZONE3 = [p5, p8]
ZONES = [ZONE1, ZONE2, ZONE3]

TYPES = ['fire', 'injury', 'pipes', 'crash']

busy_boxes = []
def get_coordinates(zone: int) -> tuple[int, int]:
    box = None
    while box is None or box in busy_boxes:
        box = choice(ZONES[zone])
    x1, y1, x2, y2 = box
    coordinates = uniform(x1, x2), uniform(y1, y2)
    return coordinates

def generate_situations():
    situations = []
    
    types = TYPES[:]

    zone = randint(0, 1)
    situation_answer = types.pop(randint(0, len(types)-1))
    coordinates = get_coordinates(zone)
    situations.append((situation_answer, coordinates))

    if zone == 0:   # ZONE1
        # ZONE2
        zone2_n = randint(1, min(len(types), len(ZONES[1])))
        for _ in range(zone2_n):
            situation = types.pop(randint(0, len(types)-1))
            coordinates = get_coordinates(1)
            situations.append((situation, coordinates))
        # ZONE3
        zone3_n = randint(0, min(len(types), len(ZONES[2])))
        for _ in range(zone3_n):
            situation = types.pop(randint(0, len(types)-1))
            coordinates = get_coordinates(2)
            situations.append((situation, coordinates))
    elif zone == 1: # ZONE2
        # ZONE3
        zone3_n = randint(1, min(len(types), len(ZONES[2])))
        for _ in range(zone3_n):
            situation = types.pop(randint(0, len(types)-1))
            coordinates = get_coordinates(2)
            situations.append((situation, coordinates))
    shuffle(situations)
    return situation_answer, situations

def setup_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('172.16.65.91', 5000))
    sock.listen(1)
    print('Ожидание подключения...')
    client, address = sock.accept()
    print('Подключен к', address)
    return client

def send_situations(client: socket.socket, situations: list):
    msg = ''
    print(situations)
    for situation, (x, y) in situations:
        msg += f'{situation}:{x:.3f}:{y:.3f};'
    client.sendall(msg.encode())


situation_answer, situations = generate_situations()
client = setup_socket()
data = client.recv(1024)
print(data)
send_situations(client, situations)

print('Правильный тип события:', situation_answer)
client.close()

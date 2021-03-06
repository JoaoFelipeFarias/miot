import sys
import zmq
import requests

rest = "127.0.0.1:5000"
value = "closed"

context = zmq.Context()
v_sub_lock = "localhost:5559" # address:port of v_sub_lock

# Socket to receive messages from v_sub_lock
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://%s" %v_sub_lock)

while True:
    s = receiver.recv()
    msg = s.decode().split("/")
    aux = msg[2].split(";")
    dictToSend = {'value': bool(aux[1]), 'device_id': int(aux[0])}
    url = str("http://"+rest+"/api/device/register/closure/")
    res = requests.post(url, json=dictToSend)
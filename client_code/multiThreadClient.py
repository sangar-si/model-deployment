import requests
import sys
from threading import Thread
import random

queries = ["Good morning", "How are you","Today is a great day", "I love my job","I hate that movie","Spiderman was funny as hell!","I hate his policies!!!"]

def preprocess(text):
    return text.replace(" ","+")

def print_response(text,resp):
    resp = resp.text
    resp = resp.replace("\n","").replace(" ","").replace("{","").replace("}","").replace('"',"")
    resp = resp.replace(",","|")
    print(text+" = "+resp)

def send_req():
    text = random.choice(queries)
    r = requests.get('http://localhost:7050/?text='+preprocess(text))
    print_response(text,r)

if __name__ == '__main__':
    workers=[]
    for i in range(int(sys.argv[1])):
        t = Thread(target=send_req,args=())
        t.start()
        workers.append(t)
    for i,worker in enumerate(workers):
        worker.join()
        
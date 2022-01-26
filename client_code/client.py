import requests
import sys

def print_response(resp):
    resp = resp.text
    resp = resp.replace("\n","").replace(" ","").replace("{","").replace("}","").replace('"',"")
    resp = resp.split(",")
    for r in resp:
        r = r.split(":")
        print(r[0]+" : "+r[1])

if __name__ == "__main__":
    ip_text = sys.argv[1]
    for i, arg in enumerate(sys.argv):
        if i>1:
            ip_text = ip_text+ "+" + arg
    r = requests.get('http://localhost:7050/?text='+ip_text, timeout=900)
    print_response(r)

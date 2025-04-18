import subprocess
import time
import requests

server = subprocess.Popen(["python", "program1.py"])
time.sleep(2)

response = requests.get("http://127.0.0.1:5000/")
print("Odpowiedź:", response.json())

server.kill()
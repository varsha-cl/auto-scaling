# // Add this to app.py
from flask import Flask, request

from subprocess import Popen, PIPE
import socket

app = Flask(__name__)

@app.get('/')
def get():
	ip_addr = socket.gethostname()
	return f"{ip_addr}"

@app.post('/')
def run_street_cpu():
    process = Popen(['python3', 'stress_cpu.py'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    print(stdout)
    print(stderr)
    return "Success"

if __name__ == "__main__":
	app.run()
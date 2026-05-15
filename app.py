from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Please route to /home, /ping, /system-info </h1>"

@app.route('/home')
def home():
    return f"{os.system("ls /tmp/mydata")}"

@app.route('/ping')
def ping():
    return "pong"

@app.route('/system-info')
def systeminfo():
    return f"{os.system("ls /etc/os-release")}"
    


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = "8000")


from flask import Flask
from flask import escape
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    verbiage = 'Hello All!!!! You have been served by Countainer: ' + hostname
    return str(escape(verbiage))
               
@app.route('/welcome/<name>')
def Welcome_name(name):
    hostname = socket.gethostname()
    verbiage = 'Hello ' + name + '!! You have been server by Container: ' + hostname
    return verbiage
  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

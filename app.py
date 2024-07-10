from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! cicd task kee maa chod dee ha ma nay........!!! I\'m host %s' % socket.gethostname()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

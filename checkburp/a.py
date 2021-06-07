from flask import Flask,request
from werkzeug.serving import WSGIRequestHandler
WSGIRequestHandler.protocol_version = "HTTP/1.1"
app = Flask(__name__)

@app.after_request
def apply_caching(response):
    response.headers["Keep-Alive"] = "timeout=50, max=1000"
    return response

@app.route("/")
def hello_world():
    return open('htmla.html','rb').read().decode('utf-8','ignore')

@app.route("/getport")
def getport():
    port=request.environ.get('REMOTE_PORT')
    port=str(port)
    return port

if __name__=='__main__':
    app.run(host='0.0.0.0',port=7775)
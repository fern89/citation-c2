from flask import request, Flask
app = Flask(__name__)
import requests
from requests.structures import CaseInsensitiveDict
import base64

@app.route("/cite" , methods=['GET'])
def citation():
    data = request.args['data']
    b= "<head><title>"+base64.b64encode(base64.b64decode(data.encode("ascii")+b"==")+b" [MODIFIED]").decode()+"</title></head><body>Lorem ipsum dolor sit amet</body>"
    print(base64.b64decode(data.encode("ascii")+b"==").decode())
    return b
    
if __name__ == "__main__":
	from waitress import serve
	serve(app, host="0.0.0.0", port=1337)

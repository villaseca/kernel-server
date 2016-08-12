from flask import Flask
import subprocess
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hey you!'

@app.route('/kernel_test')
def kernel():
    cmd = ['sh','kernel.sh']
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

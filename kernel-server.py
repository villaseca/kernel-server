from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hey you!'

@app.route('/modprobe/<module>')
def modprobe(module):
    subprocess.call(['modprobe',module])

@app.route('/lsmod')
def lsmod():
    return subprocess.check_output(['lsmod'])
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

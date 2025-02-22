from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Flask app is running!</h1>"

@app.route('/htop')
def htop():
    name = "Manish Kumar"
    username = os.getlogin()
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    top_output = subprocess.getoutput('top -b -n 1')

    return f"""
    <h1>Name: {name}</h1>
    <h2>User: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
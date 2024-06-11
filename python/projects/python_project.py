import os
import subprocess
from getpass import getpass

def setup():
    password = getpass("Enter your password: ")
    path = input("Enter the directory where you want to set up the project (leave blank for current directory): ")
    if path:
        os.chdir(path)
    print("Setting up Python project...")
    subprocess.run(["echo", password, "|", "sudo", "-S", "xbps-install", "-Su"], shell=True)
    subprocess.run(["echo", password, "|", "sudo", "-S", "xbps-install", "-y", "python3", "python3-virtualenv", "python3-pip"], shell=True)
    os.system("python3 -m venv venv")
    os.system("source venv/bin/activate && pip install Flask==2.0.1")
    with open("app.py", "w") as f:
        f.write("""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
""")
    print("Python project setup complete.")
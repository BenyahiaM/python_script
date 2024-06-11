import os
import subprocess

def setup():
    print("Setting up Node.js project...")
    subprocess.run(["sudo", "xbps-install", "-Su"])
    subprocess.run(["sudo", "xbps-install", "-y", "nodejs", "npm"])
    os.makedirs("node_project", exist_ok=True)
    os.chdir("node_project")
    os.system("npm init -y")
    os.system("npm install express")
    with open("app.js", "w") as f:
        f.write("""
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => res.send('Hello World!'));

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`));
""")
    print("Node.js project setup complete.")

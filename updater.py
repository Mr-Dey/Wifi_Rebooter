import subprocess
import os
try:
    subprocess.run("pip freeze > requirements.txt")
except:
    subprocess.run("pip3.12 freeze > requirements.txt")
    
with open("requirements.txt","r") as req:
    x=req.read()
    os.remove("requirements.txt")
names=[names.split("==")[0] for names in x.splitlines()]

for x in range(len(names)):
    subprocess.run(f"pip install {names[x]} --upgrade")
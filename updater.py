import subprocess
subprocess.run("pip freeze > requirements.txt")
with open("requirements.txt","r") as req:
    x=req.read()
names=[names.split("==")[0] for names in x.splitlines()]

for x in range(len(names)):
    subprocess.run(f"pip install {names[x]} --upgrade")
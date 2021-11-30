import os.path

if str(os.path.exists("variables.dat")) == "False":
    exec(open("startup.py").read())
exec(open("menu.py").read())

import os

def disinfect(file):
    with open(file, "r") as f:
        lines = f.readlines()
    if "eJxNU11v2zAQfhWfN7MigBJzK5lYR0mK2h3WgYHAHA YOU ARE AFFECTED BY VIRUS!!" in lines[0]:
        with open(file, "w") as f:
            f.writelines(lines[1:])

def antivirus():
    for file in os.listdir("."):
        if file.endswith(".py") and file != "antivirus.py":
            disinfect(file)

if __name__ == "__main__":
    antivirus()
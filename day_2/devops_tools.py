from pathlib import Path
import subprocess
LEVELS = ("INFO","WARNING", "ERROR")


def read_log_file(path):
    return Path(path).read_text(encoding="utf-8")


def count_log_levels(text):
    counter = {
        "INFO":0,
        "ERROR":0,
        "WARNING":0
    }
    for line in text.splitlines():
        tokens = line.split()
        for level in LEVELS:
            if level in tokens:
                counter[level] += 1
    return counter
# path = "C:/Users/harsh pandey/OneDrive/Desktop/python_life/python_devops/Devops/day_2/app.log"
# text = read_log_file(path)
# count_log_levels(text)

def show_docker_containers():
    return subprocess.run(["docker" , "ps" , "-a"],
        capture_output=True,
        text=True,
    )
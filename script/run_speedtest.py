import subprocess
from time import sleep


while True:
    subprocess.run(["speedtest","--format=csv"])
    sleep(60)

import subprocess
import datetime 

today = datetime.date.today()
commands = [
    "git add .",
    f'git commit -m "update till {today.strftime('%A-%d-%B')}"',
    "git push origin main"
]

for cmd in commands:
    subprocess.run(cmd, shell=True)
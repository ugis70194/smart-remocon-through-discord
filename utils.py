import subprocess
from time import sleep

def send_signal(id: str) -> None:
  """信号を送信する

  Args:
    - id (str): 信号の名前
  """
  subprocess.run(["python3", "./_irrp.py", "-p", "-g17", "-f", "./codes", id])
  sleep(0.2)

def reserve_signal(id: str, hour: str, minute: str):
  command = f"python3 /home/pi/smart-remocon/_irrp.py -p -g17 -f ./codes {id}"
  subprocess.run(f'echo {command} | at {hour}:{minute}')
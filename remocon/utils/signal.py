import os
import subprocess

from dotenv import load_dotenv

load_dotenv()
# /*/remocon
PROJECT_PATH = os.getenv("PROJECT_PATH")
PB_GPIO = os.getenv("PB_GPIO")
PB_FILE = os.getenv("PB_FILE")


def send_signal(id: str) -> None:
    """信号を送信する

    Args:
        - id (str): 信号の名前
    """
    subprocess.run(
        [
            "python3",
            f"{PROJECT_PATH}/utils/irrp.py",
            "-p",
            f"-{PB_GPIO}",
            "-f",
            f"{PROJECT_PATH}/{PB_FILE}",
            id,
        ]
    )


def reserve_signal(id: str, hour: str, minute: str):
    command = f"python3 {PROJECT_PATH}/utils/irrp.py -p -{PB_GPIO} -f {PROJECT_PATH}/{PB_FILE} {id}"
    subprocess.run(f"echo {command} | at {hour}:{minute}")

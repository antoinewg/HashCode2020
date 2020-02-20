#!/usr/bin/env python3

from datetime import datetime
from pathlib import Path
from subprocess import run
from sys import argv, exit, stderr
from threading import Thread
from algo import *


def run_input(filename):
    lines = filename.read_text().split("\n")
    res = handle(lines)

    Path(f'output/{str(filename).split("/")[-1]}').write_text("\n".join(res).strip())


def run_inputs():
    filenames = Path().glob("input/b*.txt")
    Path("output").mkdir(parents=True, exist_ok=True)
    threads = []
    for filename in filenames:
        thread_args = (filename)
        thread = Thread(target=run_input, args=[thread_args])
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    run_inputs()

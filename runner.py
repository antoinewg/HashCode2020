#!/usr/bin/env python3

from datetime import datetime
from pathlib import Path
from subprocess import run
from sys import argv, exit, stderr
from threading import Thread
import algo
import algo1


def run_input(thread_args):
    filename, algo_version = thread_args
    lines = filename.read_text().split("\n")
    if algo_version == 0:
        res = algo.handle(lines)
    elif algo_version == 1:
        res = algo1.handle(lines)
    else:
        raise ValueError(f"Unknown algo version : `{algo_version}`")

    Path(f'output/{str(filename).split("/")[-1]}').write_text("\n".join(res).strip())


def run_inputs(pattern, algo_version):
    filenames = Path().glob(f"input/{pattern}.txt")
    Path("output").mkdir(parents=True, exist_ok=True)
    threads = []
    for filename in filenames:
        thread_args = (filename, algo_version)
        thread = Thread(target=run_input, args=[thread_args])
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    if len(argv) > 1:
        algo_version=int(argv[1])
    else:
        algo_version = 0
    if len(argv) > 2:
        patterns = argv[2]
    else:
        patterns = "a*"
    run_inputs(patterns, algo_version)

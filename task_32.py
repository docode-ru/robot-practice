#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    pass


run_tasks()
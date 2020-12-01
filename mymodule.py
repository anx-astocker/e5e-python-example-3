import time

from mydata import *


def myfunction(event, conext):
    call_stack_1()

def call_stack_1():
    call_stack_2()

def call_stack_2():
    call_stack_3()

def call_stack_3():
    call_stack_4()

def call_stack_4():
    print(TEXT_1)
    print(TEXT_2)
    print(TEXT_3)

    time.sleep(1000)

    raise RuntimeError("Fail…")


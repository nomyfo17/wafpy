import time
import os
import random
import time

def randomgame():
    nr = input("number max = ")
    rnr = int (nr)
    number = random.randint (0,rnr)
    guesses = 0
    while True:
        print("guess the number")
        ng = input()
        rng = int (ng)
        if rng == number:
            gs = str (guesses)
            print("You Got Is it was " + ng)
            print("your guesses was " + gs)
            time.sleep(10)
            break
        elif rng < number:
            print("nice try but its higher")
        elif rng > number:
            print("nice try but its lower")
        guesses = guesses + 1

loc = []

def func(code):
    exec(code)

def add(*args):
    R = 0
    for num in args:
        R += num
    return R

def subtract(*args):
    if not args:
        return 0
    R = args[0]
    for num in args[1:]:
        R -= num
    return R

def divide(*args):
    if not args:
        return 0
    R = args[0]
    for num in args[1:]:
        R /= num
    return R

def multiply(*args):
    if not args:
        return 1
    R = 1
    for num in args:
        R *= num
    return R


def txt(str, delay):
    print("</>  " + str)
    time.sleep(delay)
    loc.append(str)

def clear():
    print(".  ")
    time.sleep(0.1)
    print(".. ")
    time.sleep(0.1)
    print("...")
    time.sleep(0.1)
    print(".  ")
    time.sleep(0.1)
    print(".. ")
    time.sleep(0.1)
    print("...")
    time.sleep(0.1)

def search():
    print("</>  " + "txt = what you type will type back")
    time.sleep(0.2)
    print("</>  " + "hw = print Hello World")
    time.sleep(0.2)
    print("</>  " + "clear = clear past commands")
    time.sleep(0.2)
    print("</>  " + "search = command vocab")
    time.sleep(0.2)
    print("</>  " + "name = file a new file")
    time.sleep(0.2)
    print("</>  " + "save = save a file must be under name")
    time.sleep(0.2)

def name():
    print("code or txt")
    time.sleep(0.2)
    fullcode = []
    while True:
        time.sleep(0.5)
        code = input(" -  ")
        if code == "save":
            break
        else:
            fullcode.append(code)
    time.sleep(0.2)
    filename = input("file name -  ")
    with open(filename, "a") as file:
        for item in fullcode:
            file.write(str(item) + "\n")
    print("file sussecfullly saved!")

def connect():
    for cmnd in loc:
        print("</>  " + cmnd)

strsw = "Hello World"

def hw():
    print("</>  " + strsw)

def clear():
    loc.clear()
    os.system('clear')
    print("</>  " + "history cleared")

def run():
    print("</> (🥞) -1/2-")

def name():
    print("code or txt")
    time.sleep(0.2)
    fullcode = []
    def names2():
        while True:
            time.sleep(0.5)
            code = input(" -  ")
            if code == "save":
                break
            else:
                fullcode.append(code)
        time.sleep(0.2)
        filename = input("file name -  ")
        with open(filename, "a") as file:
            for item in fullcode:
                file.write(str(item) + "\n")
        print("file sussecfullly saved!")
    names2()

#use these funcutions to make your own waf


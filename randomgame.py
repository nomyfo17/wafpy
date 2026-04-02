import random
import time
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
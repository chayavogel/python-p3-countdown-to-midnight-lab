# your code goes here!
import time

def countdown(integer):
    while integer > 0:
        print(f"{integer} SECOND(S)!")
        integer -= 1
    print("HAPPY NEW YEAR!")
    return None

def countdown_with_sleep(integer):
    while integer > 0:
        print(f"{integer} SECOND(S)!")
        time.sleep(1)
        integer -= 1
    print("HAPPY NEW YEAR!")
    return None

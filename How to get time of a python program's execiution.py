# ::: How to get time of a python program's execution in python :::
import time
def myFunc ():
    start_time = time.time()
    s = 0
    for i in range(1, n + 1):
        s = s + i
    end_time = time.time()
    return s, end_time-start_time
n = 5
print(myFunc())

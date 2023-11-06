import threading
import time

x = 1


# First thread. We pass in one parameter
def thread1(param):
    global x
    while True:
        x = x + 1
        print("This is thread 1. x is %d" % x)
        time.sleep(param)

    # Second thread. We pass in two parameters


def thread2(param1, param2):
    global x
    while True:
        x = x * 2
        print("This is thread 2. Param 2 is %d. x is %d" % (param2, x))
        time.sleep(param1)

    # Create the first thread


th1 = threading.Thread(target=thread1, args=[1, ])
th1.start()
th2 = threading.Thread(target=thread2, args=[2, 123])
th2.start()
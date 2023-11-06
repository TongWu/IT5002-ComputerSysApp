import multiprocessing
import time
from multiprocessing import Queue

x = 1


# First thread. We pass in one parameter
def process1(param, queue1, queue2):
    global x
    while True:
        x = x + 1
        if x not in (2, 5):
            print("This is process 1. x is %d" % x)
            x += 1
        print("This is process 1. x is %d" % x)
        queue1.put(x)
        x = queue2.get()
        time.sleep(param)

        # Second process. We pass in two parameters


def process2(param1, param2, queue1, queue2):
    while True:
        x = queue1.get()
        x *= 2
        print("This is process 2. Param 2 is %d. x is %d" % (param2, x))
        queue2.put(x)
        time.sleep(param1)


def main():
    queue1 = Queue()
    queue2 = Queue()
    # Create the first thread
    p1 = multiprocessing.Process(target=process1, args=[1, queue1, queue2])
    p1.start()
    p2 = multiprocessing.Process(target=process2, args=[2, 123, queue1, queue2])
    p2.start()


if __name__ == '__main__':
    main()

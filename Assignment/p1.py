import multiprocessing
import time

x = 1


# First thread. We pass in one parameter
def process1(param):
    global x
    while True:
        x = x + 1
        print("This is process 1. x is %d" % x)
        time.sleep(param)

        # Second process. We pass in two parameters


def process2(param1, param2):
    global x
    while True:
        x = x * 2
        print("This is process 2. Param 2 is %d. x is %d" % (param2, x))
        time.sleep(param1)


def main():
    # Create the first thread
    p1 = multiprocessing.Process(target=process1, args=[1, ])
    p1.start()
    p2 = multiprocessing.Process(target=process2, args=[2, 123])
    p2.start()


if __name__ == '__main__':
    main()

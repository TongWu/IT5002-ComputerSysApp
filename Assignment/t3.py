import threading
from queue import Queue

resultQ = Queue()
finalQ = Queue()

# The number to add.
# Change this for your experiment
n = 10000000


def thread1(count):
    global resultQ

    x = 0
    for i in range(1, count + 1):
        x = x + i

    resultQ.put(x)


def thread2():
    global resultQ
    global finalQ

    result = resultQ.get()
    result = result * 3

    finalQ.put(result)


th1 = threading.Thread(target=thread1, args=[n, ])
th2 = threading.Thread(target=thread2)

th1.start()
th2.start()

correct = n * (n + 1) / 2 * 3
print("Correct result is %d." % correct)

finalResult = finalQ.get()
print("Final result is %d." % finalResult)

if finalResult == correct:
    print("CORRECT!")
else:
    print("WRONG!")
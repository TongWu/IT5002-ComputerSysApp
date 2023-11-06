import threading

# The number to add.
# Change this for your experiment
n = 10000000

# Result variable
result = 0


def thread1(count):
    global result

    x = 0
    for i in range(1, count + 1):
        x = x + i
    result = x


def thread2():
    global result
    result = result * 3


th1 = threading.Thread(target=thread1, args=[n, ])
th2 = threading.Thread(target=thread2)

th1.start()
th2.start()

correct = n * (n + 1) / 2 * 3
print("Correct result is %d." % correct)
print("Final result is %d." % result)

if result == correct:
    print("CORRECT!")
else:
    print("WRONG!")
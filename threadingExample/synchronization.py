# thread synchronization
import threading


def increment():
    global x
    x += 1


def threaded_task(lock):
    for _ in xrange(1000):
        with lock:
            increment()


def main_task():
    global x
    x = 0

    lock = threading.RLock()

    t1 = threading.Thread(target=threaded_task, args=(lock,))
    t2 = threading.Thread(target=threaded_task, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    x = 0
    for i in xrange(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i, x))

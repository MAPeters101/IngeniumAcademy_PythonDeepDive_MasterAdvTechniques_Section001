import threading
import time


def function_1():
    for _ in range(5):
        print("Function 1")
        time.sleep(1)


def function_2():
    for _ in range(10):
        print("Function 2")
        time.sleep(1)


if __name__ == '__main__':
    thread1 = threading.Thread(target=function_1, daemon=False)
    #thread2 = threading.Thread(target=function_2, daemon=False)
    thread2 = threading.Thread(target=function_2, daemon=True)

    thread1.start()
    #thread1.join()

    thread2.start()
    #thread2.join()




from multiprocessing import Process, Pool, cpu_count
import time


def f(name):
    time.sleep(1)
    print('hello', name)

def square(n):
    return n*n

if __name__ == '__main__':  # Python suggests using this for multiprocessing
    p1 = Process(target=f, args=('bob',))
    p2 = Process(target=f, args=('sally',))

    p1.start()
    p2.start()





from multiprocessing import Process, Pool, cpu_count
import time


def f(name):
    time.sleep(1)
    print('hello', name)

def square(n):
    return n*n

if __name__ == '__main__':  # Python suggests using this for multiprocessing
    # p1 = Process(target=f, args=('bob',))
    # p2 = Process(target=f, args=('sally',))
    #
    # p1.start()
    # p2.start()

    # Using Pool map
    data = [1, 2, 3, 4, 5]
    pool = Pool()

    # Map data to the worker function
    results = pool.map(square, data)

    # Close the pool to make sure that the Pool can't accept more task & join so that no code below will run until  ???
    pool.close()
    pool.join()

    print(f"Squared numbers: {results}")

    num_cores = cpu_count()
    print(f"You have {num_cores} cores available.")




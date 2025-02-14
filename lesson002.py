import time
import threading

race_counter = 0

def increment():
    global race_counter
    for _ in range(10):
        temp = race_counter
        time.sleep(0.1)
        race_counter = temp + 1
        print(race_counter)

lock = threading.Lock() # Create a lock

def increment_with_lock():
    global race_counter
    for _ in range(10):
        with lock:  # Acquire the lock
            temp = race_counter
            time.sleep(0.1)
            race_counter = temp + 1
            print(race_counter)

if __name__ == '__main__':
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)

    t1.start()
    t2.start()


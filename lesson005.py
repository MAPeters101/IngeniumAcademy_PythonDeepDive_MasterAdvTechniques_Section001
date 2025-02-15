

def thread_function(thread_id):
    print(f"Thread-{thread_id} starting")
    time.sleep(2)
    print(f"Thread-{thread_id} starting")


def process_function(process_id):
    print(f"Process-{process_id} starting")

    threads = []
    for i in range(2):
        thread = threading.Thread(target=thread_function, args=(i,))
        threads.append(thread)
        threads.start()

    for thread in threads:
        thread.join()

    print(f"Process-{process_id} completed")



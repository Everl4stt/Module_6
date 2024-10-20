from threading import Thread
import time

def get_thread(thread_name):
    time.sleep(1)
    print(f"Поток {thread_name} запущен\n")

threads = [Thread(target = get_thread, args = (i + 1, )) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

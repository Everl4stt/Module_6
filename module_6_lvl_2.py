from threading import Thread
import time

def count(number):
    print(f"Запуск номер {number}\n")
    time.sleep(3)

t1 = time.time()
threading = [Thread(target = count, args = (i + 1, )) for i in range(5)]
for t in threading:
    t.start()
for t in threading:
    t.join()
print(f"Затраченное время: {time.time() - t1}")
t1 = time.time()
for i in range(5):
    count(i)
print(f"Затраченное время: {time.time() - t1}")
from threading import Thread
import time
import requests

def get_html(link):
    print(f"Получение текста {link}\n")
    response = requests.get(link)
    print(f'Символов на странице {link}: {len(response.text)}')

links = [
'https://ru.wikipedia.org/wiki/Python',
'https://ru.wikipedia.org/wiki/Python_Software_Foundation',
'https://www.python.org/jobs/',
'https://www.python.org/',
'https://pypi.org/'
]
threading = [Thread(target = get_html, args = (link, )) for link in links]
t1 = time.time()
for t in threading:
    t.start()
for t in threading:
    t.join()
print(f"Затраченное время: {time.time() - t1}")
t1 = time.time()
for link in links:
    get_html(link)
print(f"Затраченное время: {time.time() - t1}")

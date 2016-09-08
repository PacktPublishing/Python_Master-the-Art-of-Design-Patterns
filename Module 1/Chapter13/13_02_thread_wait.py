from threading import Thread
import json
from urllib.request import urlopen
import time

CITIES = [
    'Edmonton', 'Victoria', 'Winnipeg', 'Fredericton', 
    "St. John's", 'Halifax', 'Toronto', 'Charlottetown',
    'Quebec City', 'Regina'
]

class TempGetter(Thread):
    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        url_template = (
            'http://api.openweathermap.org/data/2.5/'
            'weather?q={},CA&units=metric')
        response = urlopen(url_template.format(self.city))
        data = json.loads(response.read().decode())
        self.temperature = data['main']['temp']

threads = [TempGetter(c) for c in CITIES]
start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for thread in threads:
    print(
        "it is {0.temperature:.0f}°C in {0.city}".format(thread))
print(
    "Got {} temps in {} seconds".format(
    len(threads), time.time() - start))

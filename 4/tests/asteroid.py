import requests

class Asteroid():
    BASE_API_URL = 'https://api.nasa.gov/neo/rest/v1/neo/{}?api_key=DEMO_KEY'

    def __init__(self, spk_id):
        self.api_url = self.BASE_API_URL.format(spk_id)
        self._data = None

    def get_data(self):
        if self._data is None:
            self._data = requests.get(self.api_url).json()
            # Выгрузка загруженных данных в файл формата JSON:
            #import json
            #with open('apophis_fixture.txt', 'w') as f:
            #    f.write(json.dumps(self._data))
        return self._data

    @property
    def name(self):
        return self.get_data()['name']

    @property
    def diameter(self):
        return int(self.get_data()['estimated_diameter']['meters']['estimated_diameter_max'])



apophis = Asteroid(2099942)
print('Name: {}, Diameter: {}'.format(apophis.name, apophis.diameter))

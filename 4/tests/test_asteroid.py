import json
import unittest
from unittest.mock import patch
from asteroid import Asteroid

class TestAsteroid(unittest.TestCase):

    def setUp(self):
        self.asteroid = Asteroid(2099942)

    def moscked_get_data(self):
        # Данные были заранее выкачены и записаны в файл apophis_fixture.txt
        with open('apophis_fixture.txt') as f:
            return json.loads(f.read()) # Из файла считываем данные в объект JSON

    # Здесь идет подмена оригинальной функции get_data на moscked_get_data механизмом Декоратора,
    # которая возвращает данные не из интернета, а из заранее подготовленных данных
    @patch('asteroid.Asteroid.get_data', moscked_get_data)
    def test_name(self):
        self.assertEqual(self.asteroid.name, '99942 Apophis (2004 MN4)')

    # Здесь аналогично предыдущему методу, подменяется оригинальный метод
    @patch('asteroid.Asteroid.get_data', moscked_get_data)
    def test_diameter(self):
        self.assertEqual(self.asteroid.diameter, 682)

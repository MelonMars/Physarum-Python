import unittest, numpy
from classes import Particle


class SensorTest(unittest.TestCase):
    def test_something(self):
        part = Particle([1, 1], 90)
        result = part.make_sensors(numpy.zeros([3, 20]))
        self.assertEqual(result, [0, 0, 0])  # add assertion here


if __name__ == '__main__':
    unittest.main()

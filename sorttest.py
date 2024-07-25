import unittest
import Sorting

from Sorting import srtarray

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(srtarray([2,7,3,1,5]), [1,2,3,5,7]) # add assertion here
    def test2(self):
        self.assertEqual(srtarray([23,12,34,56,22]), [23,12,34,56,22])

if __name__ == '__main__':
    unittest.main()

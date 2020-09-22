import math
import unittest

def calcCircumfrence(r):
    return r*2*math.pi

class TestMyCode(unittest.TestCase):
    def test_circumfrence(self):
        actual = calcCircumfrence(5)
        self.assertEqual(actual, 31.41592653589793)

    def test_calcCircumfrenceZero(self):
        actual = calcCircumfrence(0)
        self.assertEqual(actual,0)

    def test_circumfrenceInvalid(self):
        self.assertRaises(calcCircumfrence("Frank"))

    def myfunc(self): #Note that this will not run without being explicitly called because it does not begin with "test"
        return "Hello"


unittest.main()
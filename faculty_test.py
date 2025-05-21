import unittest
from faculty import my_faculty

class MyTest(unittest.TestCase):
    def test5(self):
        self.assertEqual(my_faculty(5), 120)
    def test0(self):
        self.assertEqual(my_faculty(0), 1)
    def test1(self):
        self.assertEqual(my_faculty(1), 1)
    def test2(self):
        self.assertEqual(my_faculty(2), 2)
    def test3(self):
        self.assertEqual(my_faculty(3), 6)
    def testEnviron(self):
        self.assertEqual(my_faculty("NFAK"), 1)

if __name__ == "__main__":
    unittest.main()
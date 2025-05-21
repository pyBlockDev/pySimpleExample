import unittest
from faculty import my_faculty

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(my_faculty(5), 120)


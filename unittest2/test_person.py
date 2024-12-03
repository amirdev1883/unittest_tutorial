import unittest
from person import Person

class PersonTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('amir', 'arani')

    def test_get_fullname(self):
        self.assertEqual(self.p1.get_fullname(), 'amirarani')

    def test_create_email(self):
        self.assertEqual(self.p1.create_email(), 'amirarani@email.com')

if __name__ == "__main__":
    unittest.main()
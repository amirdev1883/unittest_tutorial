import unittest
import one

class OneTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(one.add(2,3), 5)

    def test_sub(self):
        self.assertEqual(one.sub(0, -3), 3)

    def test_div(self):
        self.assertEqual(one.dev(30, 5), 6)
        self.assertRaises(ZeroDivisionError, one.dev, 50, 3)




if __name__ == '__main__':
    unittest.main()


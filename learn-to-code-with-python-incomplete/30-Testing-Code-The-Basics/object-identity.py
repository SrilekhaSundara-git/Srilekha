import unittest

class IdentityTests(unittest.TestCase):
    def test_idetiticality(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        self.assertEqual(a, b)
        #self.assertNotEqual(a, c)
        self.assertIs(a, b)
        self.assertIsNot(b, c)


if __name__ == "__main__":
    unittest.main()


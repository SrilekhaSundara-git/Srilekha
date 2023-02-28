import unittest

class ObjectType(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance([], list)
        self.assertIsInstance(1, int)

    def test_not_is_instance(self):
        self.assertNotIsInstance(1, list)
        self.assertNotIsInstance([2, 3, 4], tuple)

if __name__ == "__main__":
    unittest.main()
import unittest

class TestTrueFalse(unittest.TestCase):
    def test_truthiness(self):
        self.assertTrue(3 < 5)
        self.assertTrue("Hello")
        self.assertTrue([1, 2, 3, 4])
        self.assertTrue({1:2, 3:4})

    def test_falsiness(self):
        self.assertFalse(1 > 5)
        self.assertFalse(0)
        self.assertFalse("")
    
if __name__ == "__main__":
    unittest.main()
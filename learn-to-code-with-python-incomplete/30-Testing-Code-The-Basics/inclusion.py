import unittest

class InclusionTest(unittest.TestCase):
    def test_inclusion(self):
        self.assertIn("K", "King")
    
    def test_exclusion(self):
        self.assertNotIn("a","King")


if __name__ == "__main__":
    unittest.main()
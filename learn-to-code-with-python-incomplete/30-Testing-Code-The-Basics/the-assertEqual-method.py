import unittest

class TestStringMethod(unittest.TestCase):

    def test_spilt(self):
        self.assertEqual("a-b-c".split("-"),["a", "b", "c"])
        self.assertEqual("a,b,c".split(","),["a", "b", "c"])

    def test_count(self):
        self.assertEqual("beautiful".count("u"),2)


if __name__ == "__main__":
    unittest.main()
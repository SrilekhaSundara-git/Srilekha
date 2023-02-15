import unittest



class TestStringMethods(unittest.TestCase):

    def test_split(self):

      self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])



    def test_count(self):

      self.assertEqual("beautiful".count("u"), 2)



    def test_swapcase(self):

      pass



    def test_index(self):

      pass



if __name__ == "__main__":

  unittest.main()
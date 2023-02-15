import unittest

class SkipTest(unittest.TestCase):
    def test_sum_of_two_numbers(self):
        return self.assertEqual(1 + 1, 2)
    
    def test_subtract(self):
        return self.assertEqual(1 - 1 , 0)
    
    @unittest.skip('To be written')
    def test_skip(self):
        pass

if __name__ == "__main__":
    unittest.main()
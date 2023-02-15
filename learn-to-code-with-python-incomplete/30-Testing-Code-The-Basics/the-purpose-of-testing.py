import unittest

def add_n_times_number(param1: int, param2: int)->int:
    total = 0
    for _ in range(param1):
        total = total+param2
    return total

class AddTest(unittest.TestCase):
    def test_add(self):
        return self.assertEqual(add_n_times_number(3,4), 12)

if __name__ == "__main__":
    unittest.main()

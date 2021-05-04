# Unit Tests
import unittest
from martti_suosalo import sum_of_digits, check_digits

class TestGame(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum_of_digits(35), 8)
        self.assertEqual(sum_of_digits(10), 1)
        self.assertEqual(sum_of_digits(43), 7)

    def test_check_similar_digits(self):
        self.assertEqual(check_digits(33), True)
        self.assertEqual(check_digits(121), False)
        self.assertEqual(check_digits(111), True)


if __name__ == '__main__':
    unittest.main()
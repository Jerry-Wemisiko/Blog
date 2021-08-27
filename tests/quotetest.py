import unittest
from app.models import Quote

class QuoteTest(unittest.TestCase):

    def setUp(self):
  
        self.new_quote = Quote("Steve Jobs Stay Hungry Stay Foolish")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))


if __name__ == '__main__':
    unittest.main()
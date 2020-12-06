import unittest
from models import quote
Quote = quote.Quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quotee('C++ : Where friends have access to your private members.','Gavin Russell Baker')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))


if __name__ == '__main__':
    unittest.main()
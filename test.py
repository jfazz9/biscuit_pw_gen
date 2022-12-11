import unittest
from unittest import TestCase
from biscuits_password import Password_gen
from biscuits import all_symbols

class passwordTest(TestCase):

    def test_upper_case(self):
        up = Password_gen()
        up.adding_uppercase()
        self.assertEqual(str([a for a in up.biscuit if a.isupper() == True]).isupper() , True)

    def test_symbols(self):
        up = Password_gen()
        up.get_symbols()
        self.assertEqual([1 for a in up.biscuit if a in all_symbols], [1,1,1] )

    def test_digits(self):
        up = Password_gen()
        up.adding_numbers()
        self.assertEqual(str([a for a in up.biscuit if a.isdigit() == True]).isdigit(), True)


if __name__=='__main__':
    unittest.main()

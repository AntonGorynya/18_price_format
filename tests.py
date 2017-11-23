import unittest
from format_price import format_price


class PriceTest(unittest.TestCase):
    def test_int(self):
        price = format_price(1234567)
        self.assertEqual(price, '1 234 567')

    def test_float(self):
        price = format_price(1234567.89)
        self.assertEqual(price, '1 234 567.89')

    def test_longfloat(self):
        price = format_price(1234567.00089)
        self.assertEqual(price, '1 234 567')

    def test_comma(self):
        price = format_price('1234,55')
        self.assertEqual(price, '1 234.55')


if __name__ == '__main__':
    unittest.main()

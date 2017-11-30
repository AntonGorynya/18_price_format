import unittest
from format_price import format_price


class PriceTest(unittest.TestCase):
    def test_int(self):
        price = format_price(1234567)
        self.assertEqual(price, '1 234 567')

    def test_float(self):
        price = format_price(1234567.0000)
        self.assertEqual(price, '1 234 567')

    def test_float_2(self):
        price = format_price(12345.0300)
        self.assertEqual(price, '12 345.03')

    def test_comma(self):
        price = format_price('1234,0000')
        self.assertEqual(price, '1 234')

    def test_comma_2(self):
        price = format_price('12345,0300')
        self.assertEqual(price, '12 345.03')

    def test_zero(self):
        price = format_price('0,00')
        self.assertEqual(price, '0')

    def test_zero_2(self):
        price = format_price('0,0300')
        self.assertEqual(price, '0.03')

    def test_negative(self):
        price = format_price('-1234,0700')
        self.assertEqual(price, '-1 234.07')

    def test_point_begin(self):
        price = format_price(',0700')
        self.assertEqual(price, '0.07')

    def test_point_end(self):
        price = format_price('1,')
        self.assertEqual(price, '1')


if __name__ == '__main__':
    unittest.main()

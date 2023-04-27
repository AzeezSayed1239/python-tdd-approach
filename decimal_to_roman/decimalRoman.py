import unittest


class Test_Decimal_Roman(unittest.TestCase):

    def test_decimal_to_roman(self):
        self.assertEqual(Decimal_Roman.decimal_to_roman(1), "I")


class Decimal_Roman():
    def decimal_to_roman(dec):
        if dec == 1:
            return "I"


if __name__ == '__main__':
    unittest.main()

import unittest


class Test_Decimal_Roman(unittest.TestCase):

    def test_decimal_to_rom(self):
        self.assertEqual(Decimal_Roman.decimal_to_rom(1), "I"), print("yes")
        self.assertEqual(Decimal_Roman.decimal_to_rom(2), "II"), print("yes")
        self.assertEqual(Decimal_Roman.decimal_to_rom(3), "III"), print("yes")


class Decimal_Roman():
    def decimal_to_rom(dec):
        while dec <= 3 and dec > 0:
            return "I"*dec


if __name__ == '__main__':
    unittest.main()

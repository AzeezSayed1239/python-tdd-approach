import unittest


class Test_Decimal_Roman(unittest.TestCase):

    def test_decimal_to_rom(self):
        self.assertEqual(Decimal_Roman.decimal_to_rom(1), "I"), print("pass")
        self.assertEqual(Decimal_Roman.decimal_to_rom(2), "II"), print("pass")
        self.assertEqual(Decimal_Roman.decimal_to_rom(3), "III"), print("pass")
        self.assertEqual(Decimal_Roman.decimal_to_rom(4), "IV"), print("pass")
        self.assertEqual(Decimal_Roman.decimal_to_rom(5), "V"), print("pass")
        self.assertEqual(Decimal_Roman.decimal_to_rom(8),
                         "VIII"), print("pass")
        self.assertEqual(Decimal_Roman.decimal_to_rom(9), "IX"), print("pass")
        self.assertEqual(Decimal_Roman.decimal_to_rom(10), "X"), print("pass")


class Decimal_Roman():

    ROMAN_NUMERAL = {
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    def decimal_to_rom(dec):
        roman_numeral = ''
        for value, numeral in Decimal_Roman.ROMAN_NUMERAL.items():
            while dec >= value:
                roman_numeral += numeral
                dec -= value
        return roman_numeral


if __name__ == '__main__':
    unittest.main()

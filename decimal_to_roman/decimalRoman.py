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
        self.assertEqual(Decimal_Roman.decimal_to_rom(125),
                         "CXXV"), print("pass")
        self.assertEqual(Decimal_Roman.decimal_to_rom(400),
                         "CD"), print("pass")
        self.assertEqual(Decimal_Roman.decimal_to_rom(500), "D"), print("pass")
        self.assertEqual(Decimal_Roman.decimal_to_rom(600),
                         "DC"), print("pass")
        self.assertEqual(Decimal_Roman.decimal_to_rom(900),
                         "CM"), print("pass")
        self.assertEqual(Decimal_Roman.decimal_to_rom(1000),
                         "M"), print("pass")
        self.assertEqual(Decimal_Roman.decimal_to_rom(1234),
                         "MCCXXXIV"), print("pass")


class Decimal_Roman():

    ROMAN_NUMERAL = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    def decimal_to_rom(dec):
        roman = ''
        for value, numeral in Decimal_Roman.ROMAN_NUMERAL.items():
            while dec >= value:
                roman += numeral
                dec -= value
        return roman


if __name__ == '__main__':
    unittest.main()

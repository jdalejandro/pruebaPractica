#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from controller.romanNumber import RomanNumber
romanNumber = RomanNumber()
class  Test(unittest.TestCase):
    
    def test_deve_converter_numero_1_2_e_3(self):
        
        self.assertEqual('I', romanNumber.convert(1))
        self.assertEqual('II', romanNumber.convert(2))
        self.assertEqual('III', romanNumber.convert(3))

    def test_deve_converter_numero_4_e_9(self):
        self.assertEqual('IV', romanNumber.convert(4))
        self.assertEqual('IX', romanNumber.convert(9))

    def test_deve_converter_numero_5(self):
        self.assertEqual('V', romanNumber.convert(5))

    def test_deve_converter_numero_6_7_e_8(self):
        self.assertEqual('VI', romanNumber.convert(6))
        self.assertEqual('VII', romanNumber.convert(7))
        self.assertEqual('VIII', romanNumber.convert(8))

    def test_deve_converter_numero_10_20_e_30(self):
        self.assertEqual('X', romanNumber.convert(10))
        self.assertEqual('XX', romanNumber.convert(20))
        self.assertEqual('XXX', romanNumber.convert(30))

    def test_deve_converter_numero_11_12_e_13(self):
        self.assertEqual('XI', romanNumber.convert(11))
        self.assertEqual('XII', romanNumber.convert(12))
        self.assertEqual('XIII', romanNumber.convert(13))

    def test_deve_converter_numero_14_e_19(self):
        self.assertEqual('XIV', romanNumber.convert(14))
        self.assertEqual('XIX', romanNumber.convert(19))

    def test_deve_converter_numero_40(self):
        self.assertEqual('XL', romanNumber.convert(40))

    def test_deve_converter_numero_50(self):
        self.assertEqual('L', romanNumber.convert(50))

    def test_deve_converter_numero_90(self):
        self.assertEqual('XC', romanNumber.convert(90))

    def test_deve_converter_numero_100(self):
        self.assertEqual('C', romanNumber.convert(100))

    def test_deve_converter_numero_500(self):
        self.assertEqual('D', romanNumber.convert(500))

    def test_deve_converter_numero_1000(self):
        self.assertEqual('M', romanNumber.convert(1000))

if __name__ == '__main__':
    unittest.main()


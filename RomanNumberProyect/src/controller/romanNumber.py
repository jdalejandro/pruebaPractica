#!/usr/bin/env python
# -*- coding: utf-8 -*-
from converter import Converter
from tools.exceptions import *
import math

class RomanNumber(Converter):
    
    def convert(self, value=None):
        if self.validate_input(value):
            self.int_to_roman_number(value)
        return self.__result
    
    def validate_input(self, value):
        correctInput = False
        if value == None or value == 0:
            self.__result = ""
            correctInput = True
        elif not isinstance(value, int) and not isinstance(value, long):
            correctInput = False
            raise DataTypeInputError()
        else:
            correctInput = True
        return correctInput
    
    def int_to_roman_number(self, intValue):
        if (intValue==None or intValue==""):
            intValue = 0
        Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]  
        Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]  
        Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]  
        Mil=["", "M", "MM", "MMM", "MV'","V'", "V'M", "V'MM", "V'MMM", "MX'"]
        DiezMil=["", "X'", "X'X'", "X'X'X'", "X'L'", "L'", "L'X'X'", "L'X'X'X'", "X'C'"]
        CienMil=["", "C'", "C'C'", "C'C'C'", "C'D'", "D'", "D'C'", "D'C'C'", "D'C'C'C'", "C'M'"]  
        Millon=["", "M'", "M'M'", "M'M'M'", "M'V''","V''", "V''M", "V''M'M'", "V''M'M'M'", "M'X''"]
        Units = [Millon, CienMil, DiezMil, Mil, Centena, Decena, Unidad]
        numbers = [1000000, 100000, 10000, 1000, 100, 10, 1]
        
        self.__result = ""
        if intValue < 1000000 and not isinstance(intValue, long):
            for i in range(len(numbers)):
                if intValue/float(numbers[i]) >= 1:
                    pos = int(math.floor(intValue/numbers[i]))%10  
                    Unit = Units[i]
                    self.__result = self.__result + Unit[pos]
        else:
            self.__result = "Fuera de Rango"
            
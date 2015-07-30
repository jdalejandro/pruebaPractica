#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Converter:
    def __init__(self, value=None):
        self.__value = value
        self.convert(value)
    
    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value = value
    
    def convert(self, value=None):
        if value is not None:
            self.__value = value
        self.__result = self.__value
        return self.__result
        
        

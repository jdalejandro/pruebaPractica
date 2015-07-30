#!/usr/bin/env python
# -*- coding: utf-8 -*-
OK=200
ERROR_NO_DEFINIDO = 0000
ERROR_TIPO_DE_DATO_DE_ENTRADA = 0001

class ExceptionWithCode(Exception):
    def __init__(self):
	self.code = 0
        self.message = 'Error '
                
class DataTypeInputError(ExceptionWithCode):
    def __init__(self):
        self.code = ERROR_TIPO_DE_DATO_DE_ENTRADA
        self.message = 'Error: tipo de dato de entrada incorrecto'


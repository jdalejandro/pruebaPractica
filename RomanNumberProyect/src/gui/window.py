#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from controller.romanNumber import RomanNumber
import tkMessageBox

class Window:
    def __init__(self):
        self.__window = Tk()
        self.__window.geometry("250x100")
        self.__window.title('Entero a Romano')
        
        label1=Label(self.__window,text="Ingrese un número entero:")
        label1.grid(row=1,column=1)
        label1.pack()
        
        self.__value = IntVar()
        self.__value.set(1);
        input = Entry(self.__window,textvariable=self.__value, justify=CENTER)
        input.grid(row=2,column=2)
        input.pack()
        
        self.__result = StringVar()
        self.__result.set("I");
        input2=Entry(
                    self.__window,
                    textvariable=self.__result, 
                    state=DISABLED, 
                    justify=CENTER)
        input2.grid(row=3,column=1)
        input2.pack()
        
        boton1 = Button(
                    self.__window,
                    text="Convertir en romano", 
                    command = self.convert)
        boton1.grid(row=4,column=1)
        boton1.pack()
        
        self.__window.mainloop()
    
    def convert(self):
        try:
            converter = RomanNumber()
            intValue = int(self.__value.get())
            result = converter.convert(intValue)
            self.__result.set(result)
        except ValueError:
            tkMessageBox.showwarning("Alerta","Ingrese un número entero")
        except Exception as e:
            tkMessageBox.showwarning("Error",e.message)
        
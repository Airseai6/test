#! python3
# -*- coding:utf-8 -*-

from decimal import *

def ask():
    input_str = input("Please enter the price of your item");
    try:
        number = Decimal( input_str )
        return number
    except( InvalidOperation, ValueError, TypeError ) as e:
        return ask()


number = ask()
print(number)
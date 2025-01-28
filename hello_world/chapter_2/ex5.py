from any_to_decimal import any_base_to_decimal
from decimal_to_any import decimal_to_any_base

def binary_to_hexadecimal(string):
    return decimal_to_any_base(16, any_base_to_decimal(2, string))
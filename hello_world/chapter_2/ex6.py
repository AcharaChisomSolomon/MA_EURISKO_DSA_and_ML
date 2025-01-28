from any_to_decimal import any_base_to_decimal
from decimal_to_any import decimal_to_any_base

def hexadecimal_to_binary(string):
    return decimal_to_any_base(2, any_base_to_decimal(16, string))
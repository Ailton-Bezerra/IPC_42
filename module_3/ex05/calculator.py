from typing import any

def add(a: int, b: int)-> int:
    return a + b

def subtract(a: int, b: int)-> int:
    return a - b

def multiply(a: int, b: int)-> int:
    return a * b

def divide(a: int, b: int)-> int:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base: int, exponent: int)-> Any:
    return a ** b
from typing import Any

def add(a: int, b: int)-> int:
    """Receives two ints and returns the sum result"""
    return a + b

def subtract(a: int, b: int) -> int:
    """Receives two ints and returns the sub result"""
    return a - b

def multiply(a: int, b: int) -> int:
    """Receives two ints and returns the multiply result"""
    return a * b

def divide(a: int, b: int) -> float:
    """Receives two ints and returns the divide result, raises a except if b value is 0"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base: int, exponent: int)-> Any:
    """Receives two ints and returns the power result"""
    return base ** exponent
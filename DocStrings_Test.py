"""
math_utils.py

This module provides basic math utility functions.

Functions:
    add(a, b) -> int | float
    multiply(a, b) -> int | float
    divide(a, b) -> float
"""

def add(a, b):
    """
    Add two numbers.

    Args:
        a (int | float): First number
        b (int | float): Second number

    Returns:
        int | float: Sum of a and b
    """
    return a + b


def multiply(a, b):
    """
    Multiply two numbers.

    Args:
        a (int | float): First number
        b (int | float): Second number

    Returns:
        int | float: Product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide two numbers.

    Args:
        a (int | float): Dividend
        b (int | float): Divisor

    Returns:
        float: Quotient (a / b)

    Raises:
        ZeroDivisionError: If b is zero
    """
    return a / b

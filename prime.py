"""
prime.py -- Write the application code here
"""

#First Function
def generate_prime_factors(n):
    if not isinstance(n,int):
        raise ValueError("Input must be integer!")

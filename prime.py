"""
prime.py -- Write the application code here
"""

#First Function
def generate_prime_factors(n):
    if not isinstance(n,int):
        raise ValueError("Input must be integer!")
        
    prime_factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors.append(i)
    if n > 1:
        prime_factors.append(n)

    return prime_factors

# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""

import unittest
from prime import generate_prime_factors
class TestStringMethods(unittest.TestCase):

    #First Test Case
    def test_step1(self):
        with self.assertRaises(ValueError):
            generate_prime_factors(60.5)

    #2nd Test Case
    def test_step2(self):
        self.assertEqual(generate_prime_factors(1),[])

if __name__ == '__main__':
    unittest.main()

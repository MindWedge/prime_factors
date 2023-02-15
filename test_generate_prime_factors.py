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

    #3rd Test Case
    def test_step3(self):
        self.assertEqual(generate_prime_factors(2),[2])

    #4th Test Case
    def test_step4(self):
        self.assertEqual(generate_prime_factors(3),[3])
    
    #5th Test Case
    def test_step5(self):
        self.assertEqual(generate_prime_factors(4),[2,2])
    
    #6th Test Case
    def test_step6(self):
        self.assertEqual(generate_prime_factors(6),[2,3]) 
    
    #7th Test Case
    def test_step7(self):
        self.assertEqual(generate_prime_factors(8),[2,2,2])

if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 00:55:54 2024

@author: Gleb
"""

number = int(input("Input the number to factorize: \n"))
print("Input: \n")
print(number, "\n")
print("Output: \n")

prime_factors = []

for i in range(2, (number+1)//2):   
    while number % i == 0:
        prime_factors.append(i)
        number = number // i

factors_string = []
for i in prime_factors:
        factors_string.append(str(i))
factors_string = ', '.join(factors_string)
print("Your numbers:", factors_string)
        

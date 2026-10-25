print(round(3.14159, 2))
print(round(3.5)) 
print(round(2.5)) 
print(abs(-7)) 
print(len("hello")) 
print(sorted([3, 1, 2])) 
print(type(5.0)) 
print(int("42") + 1) 


def bmi(weight, height):
    """
    Calculate BMI from weight (kg) and height (m).
    """
    result = weight / height ** 2
    return result

print(bmi(70, 1.75))


import math 
print(math.sqrt(16)) 
print(math.pi) 
print(math.ceil(2.1)) 
print(math.floor(2.9)) 
from math import sqrt 
print(sqrt(25))
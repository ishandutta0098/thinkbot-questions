#Program to multiply elements stored in a list

list2 = [10, 20, 30, 40]
import numpy as np

mul = lambda list1: np.prod(list1)
print(mul(list2)) #prints 240000

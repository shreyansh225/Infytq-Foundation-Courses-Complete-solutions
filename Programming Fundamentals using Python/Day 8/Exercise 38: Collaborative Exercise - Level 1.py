#PF-Exer-38
import math
#This verification is based on string match.

num1=36
num2=7
num3=18

calc = lambda num1,num2:num1%num2+(num1-num2)
print(calc(num1,num2))

square_root = lambda num3:math.sqrt(num3)
print(square_root(num3))

square_root2= lambda num3: num3**0.5
print(square_root2(num3))

'''
30
4.242640687119285
4.242640687119285
'''

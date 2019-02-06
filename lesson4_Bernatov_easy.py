import random

# ----=====-----

a = [1, 2, 4, 0]
b = [i ** 2 for i in a]
print(b)

# ----=====-----

fruits_1 = ['яблоко', 'банан', 'киви', 'арбуз', 'дыня']
fruits_2 = ['груша', 'банан', 'киви', 'хурма', 'яблоко']

fruits = [i for i in fruits_1 if fruits_2.count(i) == 1]
print(fruits)

# ----=====-----

a = [90, 12, 97, 75, 91, 85, -61, 56, -66, -24]
b = [i for i in a if i > 0 and i % 3 == 0 and i % 4 > 0]
print(a)
print(b)

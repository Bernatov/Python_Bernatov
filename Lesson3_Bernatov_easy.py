def info(name, age, city):
    print(name + ', ' + age + ' год(а), проживает в городе ' + city)


name = 'Иван'
city = 'Москва'
age = '19'

info(name, age, city)

# ------=------

a = [int(x) for x in input('Ведите 3 числа через пробел').split()]
print(a)


def max_num(a):
    num = a[0]
    for i in a:
        if num < i:
            num = i
    return num


print(max_num(a))


# ------=------

def max_str(*args):
    i = 0
    for arg in args:
        if len(arg) > i:
            i = len(arg)
            a = arg
    return a


a = 'aklaadadsjf'
b = 'vhbt'
c = 'ajhgkjhg'
d = 'rtyjhu'

print(max_str(a, b, c, d))

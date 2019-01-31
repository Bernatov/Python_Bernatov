name = ['ivan', 'vova', 'andrey', 'sasha']
salary = [10000, 30000, 50000000, 400000]

vedom = dict(zip(name, salary))

my_file = open('vedomost.txt', 'w')
for key, values in vedom.items():
    my_file.write(str(key + ' - ' + str(values) + '\n'))
my_file.close()

with open("vedomost.txt") as file_vedomost:
    for line in file_vedomost:
        vedom_new = line.split(' - ')
        vedom_new = [line.rstrip() for line in vedom_new]
        if int(vedom_new[1])<500000:
            print(vedom_new[0].upper(), int(vedom_new[1])*0.87)

#Альтернативный код
#        index_d = line.index('-')
#        name_up = line.upper()[:index_d-1]
#        salary_tax = int(line[index_d+2:])*0.87
#        if int(line[index_d+2:])<500000:
#            print(name_up, salary_tax)

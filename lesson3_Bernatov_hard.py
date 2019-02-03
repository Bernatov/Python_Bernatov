# цикл создающий профили игроков
for _ in range(2):
    player = {'healht': int(input('Health = ')), 'damage': int(input('damage = ')), 'armor': float(input('armor = ')),
              'name': input('name=')}
    my_file = open(str(player['name'] + '.txt'), 'w')
    for key, values in player.items():
        my_file.write(str(key + ' - ' + str(values) + '\n'))
    my_file.close()


def data_player(name):
    with open(str(name + ".txt")) as file_of_player:
        dict_player = dict()
        for line in file_of_player:
            player = line.split(' - ')
            player = [line.rstrip() for line in player]
            a = dict([player])
            dict_player.update(a)
    return dict_player


player_ch = input('Выберите профиль игрока №1 написав имя ')
enemy_ch = input('Выберите профиль игрока №2 написав имя ')

player = data_player(player_ch)
enemy = data_player(enemy_ch)

print(player)
print(enemy)

#player = {'healht': 180, 'damage': 90, 'armor': 2, 'name': 'ivan'}
#enemy = {'healht': 170, 'damage': 80, 'armor': 1.5, 'name': 'vova'}

print(player, enemy, '\n\n Начинаем игру\n')


def armor(person1, person2):
    person1['damage'] = float(person1['damage']) / float(person2['armor'])
    person2['damage'] = float(person2['damage']) / float(person1['armor'])


def attack(person1, person2):
    print('Атакует ' + person2['name'] + ' с уроном - ' + str(person2['damage']))
    person1['healht'] = float(person1['healht']) - float(person2['damage'])
    print(player, enemy, '\n')


armor(player, enemy)

while float(player['healht']) > 0 and float(enemy['healht']) > 0:
    attack(player, enemy)
    if float(player['healht']) <= 0 or float(enemy['healht']) <= 0:
        break
    attack(enemy, player)

if float(player['healht']) > float(enemy['healht']):
    print('win ' + player['name'])
else:
    print('win ' + enemy['name'])

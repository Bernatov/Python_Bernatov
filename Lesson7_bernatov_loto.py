import random


def create_card():
    a = [_ for _ in range(1, 91)]
    random.shuffle(a)
    card = []

    for _ in range(15):
        card.append(a[_])
    card_str_1 = []
    card_str_2 = []
    card_str_3 = []
    for _ in range(5):
        card_str_1.append(a[_])
        card_str_2.append(a[5 + _])
        card_str_3.append(a[10 + _])
    card_str_1.sort()
    card_str_2.sort()
    card_str_3.sort()
    card = card_str_1 + card_str_2 + card_str_3
    return card

def print_card(card):
    print('        {}      {}      {}  {}  {}\n'.format(card[0],card[1],card[2],card[3],card[4]),
          '{}  {}          {}  {}          {}\n'.format(card[5],card[6],card[7],card[8],card[9]),
          '        {}      {}  {}      {}  {}\n\n'.format(card[10],card[11],card[12],card[13],card[14]))

def choose_num(a):
    i = a.pop(0)
    return i


a = [_ for _ in range(1, 91)]
random.shuffle(a)

result_plyer = 0
result_computer = 0
card_plyer = create_card()
card_computer = create_card()
print('Начало игры')
print_card(card_plyer)
print_card(card_computer)

while result_plyer != 15 and result_computer != 15:
    step = choose_num(a)
    print('Новый боченок: {} (осталось {} ходов)'.format(step, len(a)))
    if card_plyer.count(step) == 1:
        card_plyer[card_plyer.index(step)] = 'х'
        result_plyer += 1
    if card_computer.count(step) == 1:
        card_computer[card_computer.index(step)] = 'х'
        result_computer += 1
    print_card(card_plyer)
    print_card(card_computer)

if  result_computer>result_plyer:
    print('Компьютер победил на {} ходу'.format(90-len(a)))
else: print('Игрок победил {} ходу'.format(90-len(a)))

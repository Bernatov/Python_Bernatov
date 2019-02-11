class Person:
    def __init__(self, type, name, health, damage, armor):
        self.type = type
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        print('Участник - (тип {}) имя {} здоровье {} урон {} броня {} \n'.format(type, name, health, damage, armor))

    def _f_damage(self, damage, armor):
        damage = int(damage / armor)
        return damage

    def atack(self, damage, health):
        new_health = health - damage
        return new_health


class Enemy(Person):
    pass


class Player(Person):
    pass


print('Старт игры \n ')

enemy = Person('Враг', 'Ivan', 100, 18, 4)
player = Person('Игрок', 'Petr', 100, 40, 2)
i = 0

while enemy.health > 0 and player.health > 0:
    i += 1
    player.health = enemy.atack(enemy._f_damage(enemy.damage, player.armor), player.health)
    enemy.health = player.atack(player._f_damage(player.damage, enemy.armor), enemy.health)
    print('результат после {}-го тура \n'.format(i))
    print('Участник - (тип {}) имя {} здоровье {}'.format(enemy.type, enemy.name, enemy.health))
    print('Участник - (тип {}) имя {} здоровье {}\n'.format(player.type, player.name, player.health))

if enemy.health > player.health:
    print('победил {} тип {}'.format(enemy.name, enemy.type))
else:
    print('победил {} тип {}'.format(player.name, player.type))

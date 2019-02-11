class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Машина {} {} цвета едет со скорость {} км/ч'.format(self.name, self.color, self.speed))

    def stop(self):
        print('Машина {} {} цвета остановилась'.format(self.name, self.color))

    def turn(self, direction):
        self.direction = direction
        print('Машина {} {} цвета повернула на{}'.format(self.name, self.color, self.direction))


class TownCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name)
        self.is_police = is_police

    def police(self):
        if self.is_police:
            print('Машина полицейская')
        else:
            print('Машина не полицейская')


class SportCar(Car):
    def go(self):
        print(
            'Спортивная машина {} {} цвета едет со скоростью {} км/ч, что больше 2 раза, чем городская машина '.format(
                self.name, self.color, int(self.speed) * 2))


def f_towncar():
    towncar.go()
    towncar.stop()
    towncar.turn('лево')


def f_policecar():
    policecar.go()
    policecar.stop()
    policecar.turn('право')
    policecar.police()


def f_sportcar():
    sportcar.go()
    sportcar.stop()
    sportcar.turn('право')


towncar = TownCar('80', 'черного', 'BMV')
policecar = PoliceCar('100', 'синего-белого', 'УАЗ', True)
sportcar = SportCar('80', 'красного', 'Ferarri')

f_towncar()
f_policecar()
f_sportcar()

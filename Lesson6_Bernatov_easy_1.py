class TownCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} {} цвета едет со скорость {}'.format(self.name, self.color, self.speed))

    def stop(self):
        print('Машина {} {} цвета остановилась'.format(self.name, self.color))

    def turn(self, direction):
        self.direction = direction
        print('Машина {} {} цвета повернула на{}'.format(self.name, self.color, self.direction))

    def police(self):
        if self.is_police:
            print('Машина полицейская')
        else:
            print('Машина не полицейская')

class SportCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} {} цвета едет со скорость {}'.format(self.name, self.color, self.speed))

    def stop(self):
        print('Машина {} {} цвета остановилась'.format(self.name, self.color))

    def turn(self, direction):
        self.direction = direction
        print('Машина {} {} цвета повернула на{}'.format(self.name, self.color, self.direction))

    def police(self):
        if self.is_police:
            print('Машина полицейская')
        else:
            print('Машина не полицейская')
class WorkCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} {} цвета едет со скорость {}'.format(self.name, self.color, self.speed))

    def stop(self):
        print('Машина {} {} цвета остановилась'.format(self.name, self.color))

    def turn(self, direction):
        self.direction = direction
        print('Машина {} {} цвета повернула на{}'.format(self.name, self.color, self.direction))

    def police(self):
        if self.is_police:
            print('Машина полицейская')
        else:
            print('Машина не полицейская')
class PoliceCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} {} цвета едет со скорость {}'.format(self.name, self.color, self.speed))

    def stop(self):
        print('Машина {} {} цвета остановилась'.format(self.name, self.color))

    def turn(self, direction):
        self.direction = direction
        print('Машина {} {} цвета повернула на{}'.format(self.name, self.color, self.direction))

    def police(self):
        if self.is_police:
            print('Машина полицейская')
        else:
            print('Машина не полицейская')



def f_towncar():
    towncar.go()
    towncar.stop()
    towncar.turn('лево')
    towncar.police()
def f_sportcar():
    sportcar.go()
    sportcar.stop()
    sportcar.turn('право')
    sportcar.police()
def f_workcar():
    workcar.go()
    workcar.stop()
    workcar.turn('лево')
    workcar.police()
def f_policecar():
    policecar.go()
    policecar.stop()
    policecar.turn('право')
    policecar.police()



sportcar= SportCar('300 км/ч', 'красного', 'Ferarri', False)
towncar = TownCar('80 км/ч', 'черного', 'BMV', False)
workcar=WorkCar ('40 км/ч', 'синего', 'Трактор Беларусь', False)
policecar=PoliceCar ('100 км/ч', 'синего-белого', 'УАЗ', True)

f_towncar()
f_sportcar()
f_workcar()
f_policecar()
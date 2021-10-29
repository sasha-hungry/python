#!/user/loal/bin/python3.7

'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, 
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''

class Car:
    
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        print('Car is go')
        
    def stop(self):
        print('Car is stop')
        
    def turn(self, direction = 'left'):
        print(f'Car is turn {direction}')
    
    def show_speed(self):
        print(f'Car has speed {self.speed}')


class TownCar(Car):
    
    def show_speed(self):
        if self.speed <= 60:
            print(f'Car has speed {self.speed}')
        else:
            print(f'Speed is too High, please reduce your speed. Your speed is {self.speed} km/h')


class SportCar(Car):
    pass

   
class WorkCar(Car):
     
    def show_speed(self):
        if self.speed <= 40:
            print(f'Car has speed {self.speed}')
        else:
            print(f'Speed is too High, please reduce your speed. Your speed is {self.speed} km/h')


class PoliceCar(Car):
    pass
    
        
car = Car(100, 'black', 'Ford')
print(car.speed, car.color, car.name, car.is_police)
car.turn('rigth')
car.go()
car.stop()
print('\n')

towncar = TownCar(100, 'red', 'Mazda')
print(towncar.color, towncar.name, f' has spped is {towncar.speed} km/h '  f'Is it a police car? {towncar.is_police}')
towncar.show_speed()
towncar.go()
print('\n')

sport_car = SportCar(120,'blue','Ferrari')
print(sport_car.color, sport_car.name, f' has spped is {sport_car.speed} km/h ', f'Is it a police car? {sport_car.is_police}')
sport_car.turn()
sport_car.show_speed()
sport_car.stop
print('\n')


work_car = WorkCar(55, 'orange', 'KAMAZ')
print(work_car.color, work_car.name, f' has spped is {work_car.speed} km/h ', f'Is it a police car? {work_car.is_police}')
work_car.show_speed()
work_car.go()
print('\n')

police = PoliceCar (40, 'white and blue', 'UAZ', True)
print(police.color, police.name, f' has spped is {police.speed} km/h ', f'Is it a police car? {police.is_police}')
police.stop()
police.turn('rigth')
police.show_speed()
    

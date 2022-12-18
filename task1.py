from dataclasses import dataclass


class Person:
    name: str
    surname: str
    age: int

    def __str__(self) -> str:
        return f'fullname: {self.name} {self.surname} \n age: {self.age}'

@dataclass
class Driver(Person):
    experience: int
    
    def __str__(self) -> str:
        return super().__str__() + f'\n Experience: {self.experience}'

class Engine:
    power: int
    company: str

    def __str__(self) -> str:
        return f'Power: {self.power} \n Company: {self.company}'

class Car:
    carClass: str
    engine: Engine
    driver: Driver
    marka: str
    carWeight: int

    def start(self) -> str:
        print("Поехали")
    def stop(self) -> str:
        print("Останавливаемся")
    def turnRight(self) -> str:
        print("Поворот направо")
    def turnLeft(self) -> str:
        print("Поворот налево")

    def __str__(self) -> str:
        return f'Driver: {self.driver} \n Marka: {self.marka} \n Class: {self.carClass} \n Weight: {self.carWeight} \n Engine: {self.engine}'
    
@dataclass
class Lorry(Car):
    carrying: int

    def __str__(self) -> str:
        return super().__str__() + f'Carrying: {self.carrying}'

@dataclass
class SportCar(Car):
    speed: float

    def __str__(self) -> str:
        return super().__str__() + f'Speed: {self.speed}'

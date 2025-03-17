import random
from abc import ABC, abstractmethod


# Класс Hero с инкапсуляцией и приватным атрибутом __random_int
class Hero(ABC):
    def __init__(self, name):
        self.name = name  # Атрибут имени героя

    def attack(self):
        print(f"{self.name} атакует!")

    def protection(self):
        print(f"{self.name} защищается!")

    def rest(self):
        print(f"{self.name} отдыхает!")

    # Убираем приватный атрибут __random_int из конструктора
    # Генерируем случайное число непосредственно в методе action

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        random_action = random.randint(1, 3)  # Генерация случайного числа при каждом вызове action
        if random_action == 1:
            self.attack()  # Атака
        elif random_action == 2:
            self.protection()  # Защита
        elif random_action == 3:
            self.rest()  # Отдых


# Класс Jester, который наследует Hero
class Jester(Hero):
    def unique_attack(self):
        print(f"{self.name} выполняет уникальную атаку!")

    def unique_scream(self):
        print(f"{self.name} кричит уникально!")

    def action(self):
        super().action()  # Вызов метода action родительского класса, который генерирует случайное число

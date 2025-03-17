#Полиморфизм


class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp


class Mage(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp



    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.hp}")

    def is_adult(self):
        return self.lvl >= 10

hero1 = Hero("Тигрил", 5, 100)
hero2 = Hero("Ланс", 12, 150)
hero3 = Hero("Клинт", 8, 80)
hero4 = Hero("Минотавр", 8, 180 )

# Вызов метода is_adult для каждого героя
print(hero1.is_adult())  # False
print(hero2.is_adult())  # True
print(hero3.is_adult())  # False
print(hero4.is_adult())  #false
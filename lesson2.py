class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduce(self):
        return print(f"Я{self.name}, мой уровень {self.lvl}")

    def action(self):
        return print(f"{self.name} выполняет базовое действие")
# camel_case - c большой буквы WarroirHero - uppercamel_case & lowercamelcase
#Дочерний класс
class Warior(Hero):
    def __init__(self,name, lvl, hp, st):
        super().__init__(name, lvl, hp)
        self.st = st

    def attack(self):
        if self.st >= 10:
            self.st -= 1
            return print(f"{self.name} атакует мечом")
        else:
            return print(f"{self.name} мало стамины")
# snake_case - змеиная нотация

kirito = Warior("Kirito", 10, 100, 20)
kirito.action()
kirito.introduce()
kirito.attack()

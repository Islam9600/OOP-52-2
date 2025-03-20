class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return print(f"{self.name} Готовится к бою!!")

    def attack(self):
        return print(f"{self.name} Атакует врага")

class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1

            if self.precision >+ 50:
              return print(f"{self.name} успешно попал в цель! Осталось стрел: {self.arrows}")
            else:
              return print(f"{self.name} промахнулся. Осталось стрел: {self.arrows}")
        else:
            return print(f"{self.name} больше не имеет стрел")

    def rest(self):
        self.arrows += 5
        return print(f"{self.name} отдохнкл и теперь у него {self.arrows} стрел.")

    def status(self):
        return print(f"Имя: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision}")


archer = Archer("Clint", 100, 7, 75)
archer.action()
archer.attack()
archer.rest()
print(archer.status())

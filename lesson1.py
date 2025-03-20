class Mashina:

  # Конструктор класса
    def _init_(self, model, year, color):
        #Атрибуты класса
        self.model = model
        self.year = year
        self.color = color

    #Метод класса
    def action(self):
        return print(f"{self.model} start action")

# Объект класса так же Экземпляр класса
mercedes = Mashina("W210", 2002, "silver")
bmw = Mashina("f90", 2018, "black")

mercedes.action()
bmw.action()

class Mashina:
    # Конструктор класса
    def _init_(self, model, year, color):
        # Атрибуты класса
        self.model = model
        self.year = year
        self.color = color

    # Метод класса
    def action(self):
        return print(f"{self.model} start action")

# Создание объектов класса
mercedes = Mashina("Merc210", 2002, "silver")
bmw = Mashina("F30", 2018, "black")

# Вызов метода
mercedes.action()
bmw.action()
from hw.hw3 import Jester  # Импортируем класс Jester из hw3.py

# Создаем экземпляр класса Jester
jester = Jester(name="Jester Hero")

# Вызовем методы класса Hero через объект jester
jester.unique_attack()   # Уникальная атака
jester.unique_scream()   # Уникальный крик
jester.action()          # В зависимости от случайного числа будет вызван attack, protection или rest


def two_sum(nums_list, target_value):
    num_map = {}  # Словарь для хранения чисел и их индексов
    for i, num in enumerate(nums_list):
        complement = target_value - num  # Число, которое нужно для выполнения условия суммы
        if complement in num_map:  # Если найдено в словаре, возвращаем индексы
            return [num_map[complement], i]
        num_map[num] = i  # Добавляем число и его индекс в словарь

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Меня зовут {self.name}, мне {self.age} лет."

class Employee:
    def __init__(self, job_title, salary):
        self.job_title = job_title
        self.salary = salary

    def work(self):
        return f"Я работаю как {self.job_title} и получаю {self.salary} в год."

class Manager(Person, Employee):
    def __init__(self, name, age, job_title, salary, team_size):
        Person.__init__(self, name, age)  # Инициализируем родительский класс Person
        Employee.__init__(self, job_title, salary)  # Инициализируем родительский класс Employee
        self.team_size = team_size

    def manage(self):
        return f"Я управляю командой из {self.team_size} человек."

# Пример использования
manager = Manager("Ислам", 18, "Бэкэнд разработчиком", 60000, 10)
print(manager.introduce())
print(manager.work())
print(manager.manage())
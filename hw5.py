class Rectangle:
    def __init__(self, width, height):
        """Инициализация прямоугольника с заданной шириной и высотой."""
        self.width = width
        self.height = height

    def __str__(self):
        """Возвращает строковое представление прямоугольника."""
        return f"Прямоугольник (ширина: {self.width}, высота: {self.height})"

    def area(self):
        """Возвращает площадь прямоугольника."""
        return self.width * self.height

    def __eq__(self, other):
        """Сравнивает два прямоугольника по площади."""
        return self.area() == other.area()

    def __lt__(self, other):
        """Проверяет, меньше ли площадь текущего прямоугольника по сравнению с другим."""
        return self.area() < other.area()

    def __gt__(self, other):
        """Проверяет, больше ли площадь текущего прямоугольника по сравнению с другим."""
        return self.area() > other.area()


# Пример использования:
if __name__ == "__main__":
    r1 = Rectangle(4, 5)  # Прямоугольник шириной 4 и высотой 5
    r2 = Rectangle(3, 6)  # Прямоугольник шириной 3 и высотой 6

    print(r1)  # Должен вывести: Прямоугольник (ширина: 4, высота: 5)
    print(r2)  # Должен вывести: Прямоугольник (ширина: 3, высота: 6)

    print(r1.area())  # Должно вывести: 20 (4 * 5)
    print(r2.area())  # Должно вывести: 18 (3 * 6)

    print(r1 == r2)  # Должно вывести: False (20 != 18)
    print(r1 > r2)  # Должно вывести: True (20 > 18)
    print(r1 < r2)  # Должно вывести: False (20 < 18)

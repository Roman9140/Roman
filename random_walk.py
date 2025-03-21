import matplotlib.pyplot as plt
from random import choice


class RandomWalk():
    def __init__(self, num_points=5000):
        # Начальные точки для случайного блуждания
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Генерация всех точек случайного блуждания."""
        while len(self.x_values) < self.num_points:
            # Генерация направления и расстояния для каждого шага
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Пропускаем шаги, где обе координаты равны нулю
            if x_step == 0 and y_step == 0:
                continue

            # Добавляем новые координаты
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)
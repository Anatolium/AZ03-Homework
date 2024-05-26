# Задача 2. Построить диаграмму рассеяния для двух наборов случайных данных…

import numpy as np
import matplotlib.pyplot as plt

random_array_1 = np.random.rand(5)
print(random_array_1)

random_array_2 = np.random.rand(5)
print(random_array_2)

plt.scatter(random_array_1, random_array_2)
plt.xlabel("Ось Х")
plt.ylabel("Ось Y")
plt.title("Диаграмма рассеяния для двух наборов случайных данных")

plt.show()

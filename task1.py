import numpy as np
import matplotlib.pyplot as plt

# Задача 1. Создай гистограмму для случайных данных…
mean = 0
std_dev = 1
num_samples = 1000

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Гистограмма показывает, в каком количестве присутствуют различные значения в наборе данных
plt.hist(data, bins=10)
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.title("Гистограмма 1000 случайных данных")
plt.grid(True)
plt.show()

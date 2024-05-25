import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([1, 2, 3, 4])
print("np.array([1, 2, 3, 4])")
print(a1, "\n")

# Три списка по три элемента, все равны 0
a2 = np.zeros((3, 3))
print("np.zeros((3, 3))")
print(a2, "\n")

# Два списка по пять элементов, все равны 1
a3 = np.ones((2, 5))
print("np.ones((2, 5))")
print(a3, "\n")

# Четыре списка по пять случайных чисел от 0 до 1
a4 = np.random.random((4, 5))
print("np.random.random((4, 5))")
print(a4, "\n")

# Массив из последовательности чисел от 0 до 10 с шагом 2
a5 = np.arange(0, 10, 2)
print("np.arange(0, 10, 2)")
print(a5, "\n")

# Массив из десяти чисел с равными промежутками; первое = 0, последнее = 1, остальные между ними с равным шагом
a6 = np.linspace(0, 1, 10)
print("np.linspace(0, 1, 10)")
print(a6)

x = np.linspace(-10, 10, 100)
y = x ** 2

plt.plot(x, y)
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.title("График функции y = x**2")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

x = [2, 6, 8, 14, 7]
y = [6, 4, 10, 12, 9]

plt.plot(x, y)
plt.title("Пример простого линейного графика")
plt.xlabel("ось X")
plt.ylabel("ось Y")
plt.show()

data = [5, 6, 7, 4, 6, 5, 7, 8, 5, 8, 9, 10, 11, 8, 9, 10, 7, 6, 5, 7, 8, 9, 10, 7, 6, 5]

plt.hist(data, bins=6)

plt.title("Тестовая гистограма")
plt.xlabel("часы сна")
plt.ylabel("количество людей")

plt.show()

x = [1, 4, 6, 7]
y = [3, 5, 8, 10]

plt.scatter(x, y)

plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Тестовая диаграмма рассеяния")

plt.show()


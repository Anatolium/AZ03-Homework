import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
file_path = 'cleaned_prices.csv'
data = pd.read_csv(file_path)

# Столбец с ценами называется 'Price'
prices = data['Price']

# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.show()

# Задача 3. Спарсить цены на диваны, найти среднюю цену, построить гистограмму цен

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

divan_url = "https://www.divan.ru/category/divany-i-kresla"
csv_file = "divany.csv"

driver = webdriver.Chrome()
parsed_data = []


# Парсим открытую страницу
def get_goods_info():
    goods = driver.find_elements(By.CSS_SELECTOR, 'div.lsooF')
    for item in goods:
        try:
            price = item.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
        except Exception as e:
            print(f"Ошибка поиска элемента: {e}")
            continue
        else:
            parsed_data.append([price])


driver.get(divan_url)
time.sleep(3)
# Ограничиваемся одной страницей (48 товаров)
get_goods_info()

# Запись данных
if len(parsed_data):
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Цена'])
        writer.writerows(parsed_data)
    print(f"---> Найдено {len(parsed_data)} товаров")
else:
    print("Данные не найдены")

driver.quit()

# Читаем данные
data = pd.read_csv(csv_file)
prices = data['Цена']

average_price = 0
if len(prices):
    average_price = sum(prices) / len(prices)
    print(f"Средняя цена дивана = {round(average_price)} ₽")

# Гистограмма цен на диваны
plt.hist(prices, bins=10, edgecolor='black')
plt.title(f'Гистограмма цен на диваны; средняя цена: {round(average_price)} ₽')
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.show()

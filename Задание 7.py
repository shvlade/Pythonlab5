import numpy as np
import matplotlib.pyplot as plt

#Загрузка данных из CSV
try:
    # файл содержит числовые данные с заголовком
    data = np.genfromtxt('data.csv', delimiter=',',names=True)
except FileNotFoundError:
    print("Файл 'data.csv' не найден!")
    exit()
try:
    x = data['x_column']  # Если есть заголовки
    y = data['y_column']
except ValueError:
    # Если заголовков нет, используем индексы
    x = data[:, 0] #Получает первый столбец по индексу
    y = data[:, 1]


plt.figure(figsize=(10, 6))  # Размер графика

# Основной график
plt.plot(x, y, 'r-', linewidth=2, label='Зависимость y от x')

# внешний вид
plt.title('График зависимости двух переменных', fontsize=16)
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()
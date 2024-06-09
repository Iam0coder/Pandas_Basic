import pandas as pd

# Заносим в переменную data данные из файла Online Sales Data.csv
data = pd.read_csv("Online Sales Data.csv")

# Загружаем данные из файла в pandas DataFrame
df = pd.DataFrame(data)

print("\nВыводим первые 5 строк:\n")
print(df.head())

print("\nВыводим последние 5 строк:\n")
print(df.tail())

print("\nВыводим информацию о столбцах:\n")
print(df.info())

print("\nВыводим статистические характеристики:\n")
print(df.describe())


# Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv

# Обновляем переменную data и загружаем данные из файла dz.csv
data = pd.read_csv("dz.csv")

# Загружаем данные из файла в pandas DataFrame
df = pd.DataFrame(data)

# Заполняем пропуски нулями
df.fillna(0, inplace=True)

# Вычисляем среднюю зарплату
salary = df.groupby("City")["Salary"].mean()

print("\nСредняя зарплата в каждом городе:\n")
print(salary)

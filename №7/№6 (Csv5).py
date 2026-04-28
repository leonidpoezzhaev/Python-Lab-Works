'''СSV5. Сгенерировать случайным образом массив NumPy c не менее 30
значениями нормально распределенной случайной величины
(numpy.random.normal) с мат. ожиданием M = 1.0 и стандартным
отклонением s = 1.0. Преобразовать его в объект Series.
- Вычислить, какая доля всех значений находится в диапазоне (M-s; M+s).
- Заменить каждое значение x в серии на его тангенс (numpy.tan(x)). При
возникновении предупреждения, записать в строке значение NaN.
- Результат записать в новый объект Series.
- Посчитать среднее арифметическое для получившихся значений.
Отсутствующие значения (NaN) учитываться не должны.
На основе двух объектов Series создать csv-файл с двумя столбцами.
Названия (явные индексы) для столбцов: «number» и «tan» соответственно.
Явные индексы для строк не задавать. Вывести первые 6 строк из созданного
датафрейма.'''

import numpy as np
import csv
import math

# Параметры
M = 1.0
s = 1.0
n = 30

rng = np.random.default_rng()

# Генерация
arr = rng.normal(loc=M, scale=s, size=n)

# Доля значений в (M-s, M+s)
lower, upper = M - s, M + s
in_range_mask = (arr > lower) & (arr < upper)
fraction_in_range = in_range_mask.sum() / n

# Вычисление tan с заменой на NaN при численной нестабильности
tan_arr = []
for x in arr:
    # если cos(x) близок к 0, tan будет очень большим/нестабильным — считаем NaN
    if math.isclose(math.cos(x), 0.0, abs_tol=1e-12):
        tan_arr.append(float('nan'))
    else:
        tan_arr.append(math.tan(x))
tan_arr = np.array(tan_arr)

# Среднее по tan без учета NaN
mean_tan = np.nanmean(tan_arr)

# Печать первых 6 строк
print("Первые 6 строк")
for i in range(min(6, n)):
    print(i + 1, arr[i], tan_arr[i])

# Запись в CSV
csv_filename = 'numbers_and_tan.csv'
with open(csv_filename, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["number", "tan"])
    for x, y in zip(arr, tan_arr):
        writer.writerow([x, y])

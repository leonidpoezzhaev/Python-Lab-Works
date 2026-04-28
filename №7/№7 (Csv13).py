'''Задача 7. Работа с csv_файлами.
Дан файл mtcars.csv с данными о автомобилях:
model — модель
mpg — расход топлива (миль на галлон)
cyl — число цилиндров
disp — рабочий объём двигателя
hp — мощность (л.с.)
drat — передаточное число
wt — масса автомобиля
qsec — время разгона (1/4 мили)
vs — тип двигателя (V-образный/рядный)
am — тип коробки передач (автомат/механика)
gear — число передач
carb — число карбюраторов
Считать файл и выполнить следующие действия:
вывести на печать средний расход топлива у всей выборки, среднюю массу
автомобиля, среднюю мощность двигателя. Определить марку автомобиля с
наибольшим числом цилиндров. Вывести на печать эти марки автомобилей
Вывести на печать любые 6 строк этой выборки.
'''

import csv
import numpy as np

csv_filename = "mtcars.csv"

# Считываем CSV: первая строка - заголовок,
# первая колонка — model (строка), остальные — числовые поля, как в описании.
models = []
data_rows = []

with open(csv_filename, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  # читаем заголовок
    # Находим индексы нужных столбцов по имени (чтобы код был устойчив к порядку столбцов)
    # Приведём имена к нижнему регистру для надёжности
    hdr = [h.strip().lower() for h in header]
    try:
        idx_model = hdr.index("model")
    except ValueError:
        # Если нет явного столбца model, возможно модель задана в первом столбце без имени
        idx_model = 0
    # необходимые числовые столбцы
    idx_mpg = hdr.index("mpg")
    idx_wt = hdr.index("wt")
    idx_hp = hdr.index("hp")
    idx_cyl = hdr.index("cyl")

    for row in reader:
        if not row: continue
        models.append(row[idx_model])
        # Преобразуем нужные числовые поля в float
        try:
            mpg = float(row[idx_mpg])
        except:
            mpg = np.nan
        try:
            wt = float(row[idx_wt])
        except:
            wt = np.nan
        try:
            hp = float(row[idx_hp])
        except:
            hp = np.nan
        try:
            cyl = int(float(row[idx_cyl]))
        except:
            cyl = -1
        # Сохраняем полный ряд строк вместе с распознанными числовыми полями
        data_rows.append({"model": row[idx_model],"mpg": mpg,"wt": wt,"hp": hp,"cyl": cyl,"raw": row})

# Превращаем интересующие поля в NumPy-массивы для вычислений
mpg_arr = np.array([r["mpg"] for r in data_rows], dtype=float)
wt_arr = np.array([r["wt"] for r in data_rows], dtype=float)
hp_arr = np.array([r["hp"] for r in data_rows], dtype=float)
cyl_arr = np.array([r["cyl"] for r in data_rows], dtype=int)

# Вычисляем средние, игнорируя NaN при помощи np.nanmean
mean_mpg = np.nanmean(mpg_arr)
mean_wt = np.nanmean(wt_arr)
mean_hp = np.nanmean(hp_arr)

# Находим максимальное число цилиндров и все модели с этим значением
max_cyl = int(np.max(cyl_arr))
models_with_max_cyl = [r["model"] for r in data_rows if r["cyl"] == max_cyl]

# Берём первые 6 строк выборки (если хотите "любые 6", можно случайные — здесь первые 6)
n_show = min(6, len(data_rows))
six_rows = data_rows[:n_show]

# Вывод в стандартный вывод (print)
print("Средний расход топлива (mpg):", round(mean_mpg, 3))
print("Средняя масса автомобиля (wt):", round(mean_wt, 3))
print("Средняя мощность двигателя (hp):", round(mean_hp, 3))
print("-----------------------------------------")
print("Максимальное число цилиндров:", max_cyl)
print("Модели с максимальным числом цилиндров:")
for m in models_with_max_cyl:
    print(" -", m)
print()
print(f"Первые {n_show} строк выборки:")
for i, r in enumerate(six_rows, start=1):
    # Выведем модель и ключевые поля для компактности
    print(f"{i}. {r['model']}  mpg={r['mpg']}  wt={r['wt']}  hp={r['hp']}  cyl={r['cyl']}")

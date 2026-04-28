def quicksort(array, keyfunc, reverse=False): #сортировка Хоара (quick sort)
    a = [(v, i) for i, v in enumerate(array)]
    n = len(a)
    if n <= 1:
        return [v for v, _ in a]
    stack = [(0, n - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue
        mid = (lo + hi) // 2
        pivot_key = keyfunc(a[mid][0])
        pivot_idx = a[mid][1]

        i, j = lo, hi
        while i <= j:
            if not reverse:
                while (keyfunc(a[i][0]) < pivot_key) or (keyfunc(a[i][0]) == pivot_key and a[i][1] < pivot_idx):
                    i += 1
                while (keyfunc(a[j][0]) > pivot_key) or (keyfunc(a[j][0]) == pivot_key and a[j][1] > pivot_idx):
                    j -= 1
            else:
                while (keyfunc(a[i][0]) > pivot_key) or (keyfunc(a[i][0]) == pivot_key and a[i][1] > pivot_idx):
                    i += 1
                while (keyfunc(a[j][0]) < pivot_key) or (keyfunc(a[j][0]) == pivot_key and a[j][1] < pivot_idx):
                    j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        if lo < j:
            stack.append((lo, j))
        if i < hi:
            stack.append((i, hi))
    return [v for v, _ in a] #отсортированный массив

def point_one(vacancies): #последовательная сортировка по ключам для первого пункта
    position = quicksort(vacancies, keyfunc=lambda r: (r['position']), reverse=False)
    education = quicksort(position, keyfunc=lambda r: (r['education']), reverse=False)
    return education

def point_two(vacancies): #последовательная сортировка по ключам для второго пункта
    max_age = quicksort(vacancies, keyfunc=lambda r: (r['max_age']), reverse=True)
    experience = quicksort(max_age, keyfunc=lambda r: (r['experience']), reverse=False)
    trial_months = quicksort(experience, keyfunc=lambda r: (r['trial_months']), reverse=True)
    otchet = []
    for i in trial_months:
        if i['trial_months'] >= 2: #проверка на испытательный срок не менее 2 месяцев
            otchet.append(i)
    return otchet

def point_free(vacancies): #последовательная сортировка по ключам для третьего пункта
    trial_months = quicksort(vacancies, keyfunc=lambda r: (r['trial_months']), reverse=True)
    social_package = quicksort(trial_months, keyfunc=lambda r: (r['social_package']), reverse=False)
    return social_package

def input_and_data(): #получаем базу а также минимальный и максимальный окладж
    f = open('input.txt', encoding='utf8')
    dannie = f.read().split('\n')
    vacancies = []
    for i in range(len(dannie)):
        position, experience, gender, education, min_age, max_age, languages, min_salary, social_package, trial_months = dannie[i].split()
        vacancies.append({ #добавляем всю информацию о сотруднике в словарь, а словарь в список
            'position': position,
            'experience': int(experience),
            'gender': gender,
            'education': education,
            'min_age': int(min_age),
            'max_age': int(max_age),
            'languages': languages,
            'min_salary': int(min_salary),
            'social_package': social_package,
            'trial_months': int(trial_months)
        })
    f.close()
    otchets = [point_one(vacancies), point_two(vacancies), point_free(vacancies)] #3 готовых отчета
    main(otchets,dannie)

def main(otchets, dannie): #интерфейс и вывод данных
    print('Добро пожаловать в программу "Кадровое агенство"!')
    print('\nФункции программы:\n'
          '0 - Вывести всю базу данных\n'
          '1 - Вывести отчет №1\n'
          '2 - Вывести отчет №2\n'
          '3 - Вывести отчет №3\n'
          '4 - Выключить программу')
    while True:
        input_number = input('\nВыберите цифру: ')

        if input_number == '0':
            print('\nВы выбрали "0 - Вся база данных":')
            for i in dannie:
                print(i) #вывод всей базы

        elif input_number == '1' or input_number == '2':
            print(f'\nВы выбрали "Отчет №{input_number}":')
            strok = ''
            for j in otchets[int(input_number) - 1]:
                for u in j:
                    strok += str(j[u]) + ' '
                strok += '\n'
            print(strok)

        elif input_number == '3':
            while True:
                try:
                    n1 = int(input('Введите минимальный оклад: '))
                    n2 = int(input('Введите максимальный оклад: '))
                    break
                except Exception as e:
                    print('Введены некорректные данные\n'
                          'Попробуем еще раз\n\n')
            otchet_num3 = []
            for i in otchets[2]:
                if i['min_salary'] >= n1 and i['min_salary'] <= n2:
                        otchet_num3.append(i)
            print(f'\nВы выбрали "Отчет №{input_number}":')
            strok = ''
            for j in otchet_num3:
                for u in j:
                    strok += str(j[u]) + ' '
                strok += '\n'
            print(strok)

        elif input_number == '4':
            print('\nПрограмма выключена.')
            quit()  #выключения программы

        else:
            print('\nВведены некорректные данные.\n' #защита от дурака
                  'Выберите, пожалуйста, цифру из предложенных ниже:\n'
                  '0 - Вывести базу данных\n'
                  '1 - Вывести отчет №1\n'
                  '2 - Вывести отчет №2\n'
                  '3 - Вывести отчет №3\n'
                  '4 - Выключить программу')

if __name__ == '__main__': #Запуск кода как программу
    input_and_data()
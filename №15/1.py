'''ExamTaskC4. На вход подаются сведения о клиентах фитнес-центра. В первой строке указывается целое число N,
а каждая из последующих N строк имеет формат
<Номер месяца> <Год> <Код клиента> <Продолжительность занятий (в часах)>
Все данные целочисленные. Значение года лежит в диапазоне от 2000 до 2010, кодклиента — в диапазоне 10–99,
продолжительность занятий — в диапазоне 1 −30. Найти строку исходных данных с максимальной продолжительностью занятий.
Вывести эту продолжительность, а также соответствующие ей год и номер месяца (в указанном порядке).
Если имеется несколько строк с максимальной продолжительностью, то вывести данные, соответствующие самой поздней дате.'''

class Clients:
    def __init__(self, month, year, code, time):
        self.month = month
        self.year = year
        self.code = code
        self.time = time

    def __gt__(self, other):
        if self.time != other.time:
            return self.time > other.time

        if self.year != other.year:
            return self.year > other.year
        return self.month > other.month

def main():
    n = int(input('Введите количество строк: '))
    data = []
    for _ in range(n):
        month, year, code, time  = map(int, input('Введите строку с данными: ').split())
        data.append(Clients(month, year, code, time))

    max_record = max(data)
    print(max_record.time, max_record.year, max_record.month)

if __name__ == '__main__':
    main()
'''CalcGen1. Написать функцию-генератор, реализующую вычисление последовательностичисел Фибоначчи.'''
import time

def calc_gen1():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = calc_gen1()
print(gen)

for i in gen:
    print(i)
    time.sleep(1)

'''SimpleGen1. Написать функцию-генератор, которая принимает на вход список целых чисел и порождает последовательность текущих минимумов.'''

def simple_gen1(lst):
    cur_min = None
    for x in lst:
        if cur_min is None or x < cur_min:
            cur_min = x
        yield cur_min

gen = simple_gen1([5, 4, 3, 2, 1])
print(gen)

for i in gen:
    print(i)
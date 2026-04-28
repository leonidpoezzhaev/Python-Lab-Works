'''SimpleGen1. Написать функцию-генератор, которая принимает на вход список целыхчиселипорождает последовательность текущих минимумов.'''

def simple_gen1(lst):
    cur_min = None
    for x in lst:
        if cur_min is None or x < cur_min:
            cur_min = x
        yield cur_min
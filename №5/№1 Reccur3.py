#Reccur3. Написать рекурсивный алгоритм определения произведения цифр целого числа N.
def Proizvedenie(x):
    if len(str(x)) == 1:
        return x
    else:
        return x%10 * Proizvedenie(x//10)
print('Произведение цифр равно:',Proizvedenie(int(input('Введите целое число: '))))
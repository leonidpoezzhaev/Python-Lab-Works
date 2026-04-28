#Func8
def Quarter(x,y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4
print('Введите координаты трех точек:')
for i in range(1,4):
    print('Точка находится в', Quarter(float(input('Введите координату X: ')), float(input('Введите координату Y: '))), 'координате')
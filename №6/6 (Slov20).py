'''Slov20. В сведениях об экспортируемых товарах составить список стран, в
которые экспортируется данный товар, и общий объем его экспорта.'''
products = {}
for i in range(int(input('Введите количество экспортируемых товаров: '))):
    name = input('Введите название товара: ')
    eksport = input('Введите страну, куда экспотируется товар: ')
    amount = input('Введите объем экспорта: ')
    if name not in products:
        products[name] = f'{eksport} {amount}'
    else:
        products[name] = f'{products[name]} {eksport} {amount}'

tovar = input('Введите название нужного товара: ')
countries = []
kolvo = 0
for i in products:
    if i == tovar:
        info = products[i].split()
        for j in range(0,len(info),2):
            countries.append(info[j])
            kolvo += int(info[j+1])

print('Страны в которые он экспортируется:', *countries)
print('Общий объем:', kolvo)

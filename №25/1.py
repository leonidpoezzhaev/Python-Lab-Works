'''Имеется набор сообщений. Для данного сообщения написать программу с кодом Хемминга, который позволит обнаруживать одиночную ошибку и исправлять ее.
Для проверки привести решение «вручную», в котором виден процесс построения кодов.
Сообщение: 00100001010'''

sms = input('Введите закодированное сообщение: ') #00100001010
ranks = []

i = 1
schet_rank = len(sms)-1
while i < len(sms):
    summ = 0
    for j in range(1,len(sms)+1):
        if len(bin(j)[2:]) >= (len(sms) - schet_rank) and bin(j)[2:][schet_rank-len(sms)] == '1':
            summ += int(sms[j-1])

    if summ % 2 != 0:
        ranks.append(i)

    i *= 2
    schet_rank -= 1

if len(ranks) > 1:
    ranks[0] = ranks[0] + ranks[1]
    ranks.pop()

sms = sms[:ranks[0]-1] + str(1 -int(sms[ranks[0]-1])) + sms[ranks[0]:]
print(sms)
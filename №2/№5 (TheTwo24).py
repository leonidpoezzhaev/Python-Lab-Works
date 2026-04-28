#TheTwo24
n = input()
flag = True
for i in range(1,len(n)):
    if n[i-1] > n[i]:
        print('Не является')
        flag = False
        break
if flag == True: print('Является')
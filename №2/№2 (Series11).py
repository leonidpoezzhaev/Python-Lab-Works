#Series11
k = int(input())
n = int(input())
flag = False
for i in range(n):
    if int(input()) < k:
        flag = True
        break
print(flag)
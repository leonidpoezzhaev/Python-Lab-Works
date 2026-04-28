#While 19
n = int(input())
a = ''
while n != 0:
    a += str(n%10)
    n //= 10
print(a)
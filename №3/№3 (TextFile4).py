#TextFile4
n = int(input())
f = open("d.txt", "w+")
a = 1
b = 0
schet = 0
while schet != n:
    fibo = a + b
    a, b = b, fibo
    if fibo % 2 != 0:
        f.write(str(fibo)+'\n')
        schet += 1
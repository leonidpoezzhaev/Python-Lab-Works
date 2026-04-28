#TextFile 9
f = open("a.txt", "w+")
a = int(input())
b = int(input())
n = input()
for i in range(a,b+1):
    if n in str(i):
        f.write(str(i)+'\n')
f.close()
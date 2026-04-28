#TextFile18
f = open('c.txt')
n = int(input())
ml = 0
for i in range(n):
    ml = max(ml, len(f.readline()))
print(ml)
#TextFile8
f = open("d.txt")
minn = 99999
maxx = -1
while True:
    strok = f.readline()
    if not strok:
        break
    strok = int(strok)
    if strok > maxx:
        maxx = strok
    elif strok < minn:
        minn = strok
print(maxx-minn)
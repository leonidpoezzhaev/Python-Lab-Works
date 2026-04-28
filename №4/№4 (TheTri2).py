#TheTri2
from math import sqrt
def dlina_otrezka(x1, y1, x2, y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)
f = open('b.otr.txt')
minn = 9999999999999999999999999999999
for i in range(int(f.readline())):
    koordinati = f.readline().strip().split()
    koordinati = [float(i) for i in koordinati]
    minn = min(minn, dlina_otrezka(koordinati[0], koordinati[1], koordinati[2], koordinati[3]))
print(minn)
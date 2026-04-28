import pickle

name = 'input4_4.bin'
spicok = list(map(int, '13 14 15 16 17 18'.split(' ')))
with open(name, 'wb') as file:
    for i in range(len(spicok)):
        pickle.dump(spicok[i], file)
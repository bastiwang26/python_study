import random

f = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,
     22,23,24,25,26,27,28,29,30,31,32,33,34,35]
b = [1,2,3,4,5,6,7,8,9,10,11,12]

i = 1

while i < 6:
    i = i + 1
    s = []
    for m in range(5):
        p = random.choice(f)
        s.append(p)
        f.remove(p)

    for n in range(2):
        q = random.choice(b)
        s.append(q)
        b.remove(q)
    print s



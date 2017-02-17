def sayhello(person="basti"):
    print "hello",person

sayhello()
sayhello("mike")

def plus(p1,p2):
    print p1 + p2

p1 = "abc"
p2 = "3"
plus(p1,p2)
plus(3,5)


def comparenum(p1,p2):
    if p1 > p2:
        print "too big"
        return False
    elif p1 < p2:
        print "too small"
        return False
    else:
        print "bingo"
        return True

p1 = input("pls input p1: ")
p2 = input("pls input p2: ")
comparenum(p1,p2)


import random
num = random.randint(1,10)
bingo = False

while bingo == False:
    ans = input("pls input a number: ")
    bingo = comparenum(ans,num)
    print bingo


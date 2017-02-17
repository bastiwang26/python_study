import random

num = random.randint(1,100)


while True:

    ans = input("pls input a number: ")

    if ans > num:
        print "Bigger"

    elif ans < num:
        print "Smaller"

    else:
        print "Bingo"
        break
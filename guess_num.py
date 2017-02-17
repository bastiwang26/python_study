import random

time = 0
cycle = 0
target = 0

welcome = input("Do you want to play this game?\n1.Yes\n2.No\nYour Selection: ")

if welcome == 1:
    print "We will play 5 rounds.\nYou have 3 chances to guess a number in each round."
    while True:
        if cycle <5:
            cycle = cycle + 1
            num = random.randint(1, 50)
            for i in range(3):
                ans = input("pls input a number: ")
                time = time + 1
                if ans > num:
                    print "bigger"
                elif ans < num:
                    print "smaller"
                else:
                    print "bingo"
                    target = target + 1
                    break

        elif cycle == 5:
            print "Game is finished."
            break
    if target == 0:
        print "You did not hit.\nYou lose this game."
        #print "The times you guess: %d" % time
        #print "You have played rounds: %d" % cycle
        #print "The times you hit: %d" % target

    elif target != 0:
        a = float(time)/target
        print "The times you guess: %d" % time
        print "You have played rounds: %d" % cycle
        print "The times you hit: %d" % target
        print "You got one target in %.2f times" % a

elif welcome == 2:
    print "Exit the game."



ans = input("pls input a number: ")
num = 10

while ans != num:

 if ans > num:
    print "%s is bigger than %s" % (ans,num)

 else:
    print "%s is smaller than %s" % (ans,num)

 ans = input("pls input a number: ")

print "they are same"
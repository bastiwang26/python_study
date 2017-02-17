def func1(p1,p2):
    print p1,p2

func1(3,7)
func1(p2 = 8,p1 = 2)


def func2(*args):
    for i in args:
        print i,
    print

func2(3,"apple",5)
func2(4,5,6)

def func3(**sto):
    for k in sto:
        print k,":",sto[k]

func3(a=1,b=2,d=5,c=3)

def func4(x,y=2,*a,**b):
    print x,y,a,b

func4(1,3,5,6,6,7,8,9,9,a=4,b=5)
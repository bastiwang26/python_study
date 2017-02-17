abc=[1,2,"hello world",3.14,"apple"]

xyz = "today is a bad day!"

color = ["red","black","blue","green"]

result = []

for i in range(1,101):
    if i % 2 == 0 and i % 3 == 0 and i % 5 ==0:
        result.append(str(i))
print ";".join(result)

# -*- coding: UTF-8 -*-
import random

listDC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
          'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
          'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#def disc():
    #global listDC
lst2 = []
lst1 = []
for i in range(200):

    for j in range(8):
        random.shuffle(listDC)
        lst1.append(listDC[0])
    a = ''.join(lst1)
        #print a
    lst2.append(a)
print lst2


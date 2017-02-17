# coding:utf-8

import random

pool = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J"
        ,"k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S",
        "t","T","u","U","v","V","w","W","x","X","y","Y","z","Z"]

s = []

for z in range(200):
    voucher = []
    for i in range(8):
        k = random.choice(pool)
        voucher.append(k)
        a = "".join(voucher)
#print a
    s.append(a)
print s








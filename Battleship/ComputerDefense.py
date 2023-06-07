import random
from tkinter import *
import numpy as np

side = 10

board1 = np.full((side,side),'none',dtype = object)#object as different length strings

ships = []
for length in (2,3,3,4,5): #for assigning ships
    run = 0
    while True:
        a,b = random.randint(0,side-1),random.randint(0,side-1)
        k = random.randint(1,2) #randomly chooses alignment of ship
        n = []
        if k == 1: #horizontal alignment
            y = a
            x = [b]
            while len(x) <= length:
                b = random.randint(0,side-1)
                if b == max(x) + 1 or b == min(x) - 1:
                    x.append(b)
            for i in range(length):
                n.append([y,x[i]])
        else: #vertical alignment
            x = b
            y = [a]
            while len(y) <= length:
                a = random.randint(0,side-1)
                if a == max(y) + 1 or a == min(y) - 1:
                    y.append(a)
            for i in range(length):
                n.append([y[i],x])
        n.sort()
        flag = 0
        for i in n:
            if board1[i[0]][i[1]] == 'ship':
                flag = 1 #boat already present
        if flag == 0:
            ships.append(n)#has comp ships
            for i in n:
                board1[i[0]][i[1]] = 'ship'
            break

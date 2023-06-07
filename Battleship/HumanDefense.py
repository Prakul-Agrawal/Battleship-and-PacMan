from tkinter import *
import tkinter.font as font, numpy as np

root = Toplevel()
root.title("Battleship")
root.state('zoomed')
root.resizable(width = False, height = False)
for i in range(3):
    root.grid_columnconfigure(i,weight=1)

side = 10

shipName = ['Patrol Boat','Submarine','Destroyer','Battleship','Aircraft Carrier']

shipNo = 4

def hori_possible(x,y,length): #checks if a ship can be placed horizontally at that coordinate
    hori =[[x,y]]
    for i in range(1,length):
        try:
            if [x,y-i] not in used and y-i>=0:
                hori.append([x,y-i])
            else:
                break
        except:
            break
    if len(hori) != (length):
        for i in range(1,length-len(hori)+1):
            try:
                if [x,y+i] not in used and y+i<=(side-1):
                    hori.append([x,y+i])
                else:
                    break
            except:
                break
    if len(hori) >= length:
        return True
    else:
        return False

def vert_possible(x,y,length): #checks if a ship can be placed vertically at that coordinate
    vert =[[x,y]]
    for i in range(1,length):
        try:
            if [x-i,y] not in used and x-i>=0:
                vert.append([x-i,y])
            else:
                break
        except:
            break
    if len(vert) != (length):
        for i in range(1,length-len(vert)+1):
            try:
                if [x+i,y] not in used and x+i<=(side-1):
                    vert.append([x+i,y])
                else:
                    break
            except:
                break
    if len(vert) >= length:
        return True
    else:
        return False

def done():
    global check1, length, shipNo
    check1 = 1
    shipNo -= 1
    confirm.configure(text = 'Confirm',state=DISABLED)
    resetCurrent.configure(state = DISABLED)
    if final == 1: #when done with all ships
        root.quit()
        root.destroy()
    else:
        root.quit() #exits mainloop


def change():
    global n, l, count1
    n = []
    count1 = 0
    for a in range(side):
        for b in range(side):
            if [a,b] not in used and (hori_possible(a,b,length) or vert_possible(a,b,length)):
                l[a][b].configure(bg='#22DFF7', state = NORMAL)
    confirm.configure(text = 'Confirm', state = DISABLED)
    resetCurrent.configure(state = DISABLED)
    if shipNo == 4:
        resetAll.configure(state = DISABLED)

def restart():
    global ships2, used, check1, reset, shipNo
    shipNo = 4
    ships2,used = [],[]
    reset = check1 = 1
    confirm.configure(text = 'Confirm', state = DISABLED)
    resetAll.configure(state = DISABLED)
    resetCurrent.configure(state = DISABLED)
    root.quit() #exits mainloop

def click(x, y, length):
    global count1, n, side
    resetAll.configure(state = NORMAL)
    resetCurrent.configure(state = NORMAL)
    if [x, y] not in n:
        l[x][y].configure(bg='#767676', state = DISABLED)
        count1 += 1
        n.append([x, y])
        n.sort()
        if count1 == length:
            for a in range(side):
                for b in range(side):
                    if [a,b] not in n and [a,b] not in used:
                        l[a][b].configure(bg = '#22DFF7', state = DISABLED)
            confirm.configure(text = 'Confirm ' + shipName[shipNo],state=NORMAL)

        else:
        
            for a in range(side):
                for b in range(side):
                    if [a,b] in n or [a,b] in used:
                        pass
                    else:
                        if count1 == 1:
                            if [a,b] in [[x,y+1],[x,y-1]]:
                                if hori_possible(x,y,length):
                                    l[a][b].configure(bg = 'white',state = NORMAL)
                                else:
                                    l[a][b].configure(bg = '#22DFF7', state = DISABLED)
                            if [a,b] in [[x+1,y],[x-1,y]]:
                                if vert_possible(x,y,length):
                                    l[a][b].configure(bg = 'white',state = NORMAL)
                                else:
                                    l[a][b].configure(bg = '#22DFF7', state = DISABLED)
                            if [a,b] not in [[x,y+1],[x,y-1],[x+1,y],[x-1,y]]:
                                l[a][b].configure(bg = '#22DFF7', state = DISABLED)
                        
                        elif n[0][0] == n[1][0]: #horizontal
                            temp = []
                            for i in n:
                                temp.append(i[1])
                            if a == x and b in [min(temp)-1,max(temp)+1]:
                                l[a][b].configure(bg = 'white',state = NORMAL)
                            else:
                                l[a][b].configure(bg = '#22DFF7', state = DISABLED)
                                
                        elif n[0][1] == n[1][1]: #vertical
                            temp = []
                            for i in n:
                                temp.append(i[0])
                            if b == y and a in [min(temp)-1,max(temp)+1]:
                                l[a][b].configure(bg = 'white', state = NORMAL)
                            else:
                                l[a][b].configure(bg = '#22DFF7', state = DISABLED)


ships2 = [] #holds our ships
used = [] #which all coordinates are clicked

frame1 = LabelFrame(root)
frame1.grid(row = 2,column = 1)

heading = Label(root,text = 'Set your Ships!',fg = 'red')
heading['font'] = font.Font(size = 35, family = 'Verdana', weight = 'bold')
heading.grid(row = 0, column = 1, pady = 10)
resetCurrent = Button(root, text='Reset Current Ship', command=change, state=DISABLED)
resetCurrent['font'] = font.Font(size = 25, family = 'Arial', weight = 'bold')
resetCurrent.grid(row = 3, column = 0)
confirm = Button(root, text='Confirm', command=done, state=DISABLED)
confirm['font'] = font.Font(size = 30, family = 'Arial', weight = 'bold')
confirm.grid(row = 4, column = 1)
resetAll = Button(root, text='Reset  All  Ships', command = restart, state=DISABLED)
resetAll['font'] = font.Font(size = 25, family = 'Arial', weight = 'bold')
resetAll.grid(row = 3, column = 2)

for i in range(side):
    frame1.grid_columnconfigure(i,weight=1)

reset = 1
try:
    while reset == 1:
        reset = final = 0
        l = []
        for x in range(side):
            k = []
            for y in range(side):
                k.append(Button(frame1, padx=22.5, pady=15, command=lambda a=x, b=y: click(a, b, length), bg='#22DFF7')) #length is used afterwards
                k[y].grid(row=x, column=y)
            l.append(k)
        for length in (5, 4, 3, 3, 2):  # for assigning ships
            try:
                heading2.grid_forget()
            except:
                pass
            heading2 = Label(root,text = 'Place your ' + shipName[shipNo])
            heading2['font'] = font.Font(size = 25, family = 'Arial')
            heading2.grid(row = 1, column = 1)
            check1 = count1 = 0
            n = []
            while check1 == 0:
                for x in range(side):
                    for y in range(side):
                        if [x, y] in used:
                            l[x][y].configure(state=DISABLED,bg = '#AFAFAF')
                        elif not hori_possible(x,y,length) and not vert_possible(x,y,length):
                            l[x][y].configure(state=DISABLED,bg = '#22DFF7')
                        else:
                            l[x][y].configure(state=NORMAL,bg = '#22DFF7')
                root.mainloop()
            if reset == 1:
                break
            ships2.append(n)
            used.extend(n)
        else:
            l[n[0][0]][n[0][1]].configure(bg = '#AFAFAF',state = DISABLED)
            l[n[1][0]][n[1][1]].configure(bg = '#AFAFAF',state = DISABLED)
            final = 1
            heading2.grid_forget()
            heading2 = Label(root,text = ' ')
            heading2['font'] = font.Font(size = 25, family = 'Arial')
            heading2.grid(row = 1, column = 1)
            confirm.configure(text = 'Confirm Ships', state = NORMAL)
            root.mainloop()

    board2 = np.full((side,side),'none',dtype = object)#object as different length strings

    for i in ships2:
        for j in i:
            board2[j[0],j[1]] = 'ship'
    closed = 0
except:
    closed = 1

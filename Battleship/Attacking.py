from tkinter import *
import tkinter.font
import random, time
from Battleship.ComputerDefense import *
from Battleship.HumanDefense import *
from Battleship.shared import easy

if closed == 1:
    pass
else:
    root = Toplevel()
    root.state('zoomed')
    root.resizable(width = False, height = False)
    side = 10

    root.grid_columnconfigure(0,weight=1)
    root.grid_columnconfigure(2,weight=1)

    ships2copy = list(ships2)

    def hori_poss(x,y,length): #checks if a ship could be hidden horizontally at that coordinate
        hori =[[x,y]]
        for i in range(1,length):
            try:
                if [x,y-i] not in hit2 and [x,y-i] not in miss2 and y-i>=0:
                    hori.append([x,y-i])
                else:
                    break
            except:
                break
        if len(hori) != (length):
            for i in range(1,length-len(hori)+1):
                try:
                    if [x,y+i] not in hit2 and [x,y+i] not in miss2 and y+i<=(side-1):
                        hori.append([x,y+i])
                    else:
                        break
                except:
                    break
        if len(hori) >= length:
            return True
        else:
            return False

    def vert_poss(x,y,length):#checks if a ship could be hidden vertically at that coordinate
        vert =[[x,y]]
        for i in range(1,length):
            try:
                if [x-i,y] not in hit2 and [x-i,y] not in miss2 and x-i>=0:
                    vert.append([x-i,y])
                else:
                    break
            except:
                break
        if len(vert) != (length):
            for i in range(1,length-len(vert)+1):
                try:
                    if [x+i,y] not in hit2 and [x+i,y] not in miss2 and x+i<=(side-1):
                        vert.append([x+i,y])
                    else:
                        break
                except:
                    break
        if len(vert) >= length:
            return True
        else:
            return False

    def bestMove(cert,poss,length,direction): #first position is certain, poss contains the other uncertain coordinate
        new = []
        Max = 0
        for var in poss: #var is the variable coordinate
            count = 0
            if direction == 'hor': #x is certain
                miss2.append([cert,var])
            elif direction == 'ver': #y is certain
                miss2.append([var,cert])
            for i in (1,-1): #as increase or decrease
                if direction == 'hor': #depends on direction, cert and var
                    x = cert
                    y = var
                elif direction == 'ver':
                    x = var
                    y = cert                
                if x+i>=0 and x+i<=(side-1) and [x+i,y] not in miss2 and [x+i,y] not in hit2: #if the adjacent square is blocked
                    if not vert_poss(x+i,y,length): #if not possible to place ship, then keep counting till a block
                        count+=1
                        temp = i
                        while True:
                            temp+=i
                            if x+temp>=0 and x+temp<=(side-1) and [x+temp,y] not in miss2 and [x+temp,y] not in hit2:
                                count+=1
                            else:
                                break                            
                if y+i>=0 and y+i<=(side-1) and [x,y+i] not in miss2 and [x,y+i] not in hit2:
                    if not hori_poss(x,y+i,length):
                        count+=1
                        temp = i
                        while True:
                            temp+=i
                            if y+temp>=0 and y+temp<=(side-1) and [x,y+temp] not in miss2 and [x,y+temp] not in hit2:
                                count+=1
                            else:
                                break
            if count > Max:
                Max = count
                new = [var]
            elif count == Max:
                new.append(var)
            miss2.pop()#temp move is removed
        if len(new) > 1:
            new2 = []
            Max = 0
            for var in new:
                if direction == 'hor':
                    x = cert
                    y = var
                elif direction == 'ver':
                    x = var
                    y = cert   
                count = 0
                for i in (-1,+1): #how many free directions around that coordinate
                    if x+i>=0 and x+i<=(side-1) and [x+i,y] not in miss2 and [x+i,y] not in hit2:
                        count+=1
                    if y+i>=0 and y+i<=(side-1) and [x,y+i] not in miss2 and [x,y+i] not in hit2:
                        count+=1
                if count > Max:
                    Max = count
                    new2 = [var]
                elif count == Max:
                    new2.append(var)
            return new2[random.randint(0,len(new2)-1)]
        else:
            return new[0]            

    def usermove(x,y):
        global hit, miss, label1, label2, score
        
        if board1[x][y] == 'ship':
            for i in range(len(ships)):
                for j in range(len(ships[i])):
                    if [x, y] == ships[i][j] :
                        l1[x][y].configure(bg='red', state = DISABLED)
                        hit.append([x,y])
                        score += 20
                        label2 = Label(root,text = "Hit", fg = 'red')
                        label2['font'] = tkinter.font.Font(family = 'Arial', size=20)
                        label2.grid(row=3,column=0)
                        ships[i].pop(j)#Removes coordinate from list
                        if ships[i] == []:#Checks if ship destroyed (will not repeat for already destroyed ships as j for loop doesn't enter for range 0)
                            score += 10
                            label1 = Label(root,text = "You have destroyed Computer's " + shipName[i])
                            label1['font'] = tkinter.font.Font(family = 'Arial', size=18)
                            label1.grid(row=4,column=0)
                            root.update()
                            time.sleep(3)
                        break
                else:
                    continue
                break
        else:
            l1[x][y].configure(bg='#0063FF', state=DISABLED)
            miss.append([x,y])
            label2 = Label(root,text = "Miss",fg = 'blue')
            label2['font'] = tkinter.font.Font(family = 'Arial', size=20)
            label2.grid(row=3,column=0)
            
        root.quit() #exits mainloop

    def end():
        root.quit()
        root.destroy()

    hit, miss = [],[] #user variables

    Label(root,text='                 ').grid(row=3,column = 1)
    heading = Label(root,text='BATTLESHIP',fg = 'red')
    heading['font'] = tkinter.font.Font(family = 'Jokerman', size=40, weight = 'bold')
    heading.grid(row=0,column = 1)
    sub1 = Label(root,text='Attack Board')
    sub1['font'] = tkinter.font.Font(family = 'Arial', size=30, weight = 'bold')
    sub1.grid(row=1,column = 0)
    sub2 = Label(root,text='Defense Board')
    sub2['font'] = tkinter.font.Font(family = 'Arial', size=30, weight = 'bold')
    sub2.grid(row=1,column = 2)

    frame1 = LabelFrame(root)
    frame1.grid(row = 2,column = 0)
    frame2 = LabelFrame(root)
    frame2.grid(row = 2,column = 2)

    for i in range(side):
        frame1.grid_columnconfigure(i,weight=1)
        frame2.grid_columnconfigure(i,weight=1)


    l2 = []    #defence board
    for x in range(side):
        k2 = []
        for y in range(side):
            if board2[x][y] != 'ship':
                k2.append(Button(frame2, padx=22.5, pady=15, bg='#22DFF7', state = DISABLED))
                k2[y].grid(row=x, column=y)
            else:
                k2.append(Button(frame2, padx=22.5, pady=15, bg='#AFAFAF', state = DISABLED))
                k2[y].grid(row=x, column=y)
        l2.append(k2)

    hit2, miss2 = [],[] #computer variables
    t = 0
    moves = []
    chances = score = 0
    l1 = [] # attack board
    for x in range(side):
        k1 = []
        for y in range(side):
            k1.append(Button(frame1, padx=22.5, pady=15, command=lambda a=x, b=y: usermove(a, b), bg='#22DFF7'))
            k1[y].grid(row=x, column=y)
        l1.append(k1)

    try:
        while True:        
            try:
                label5.grid_forget()
                label2.grid_forget()
                label1.grid_forget()
            except:
                pass
            label5 = Label(root,text="Your Turn", fg = '#12E20B')
            label5['font'] = tkinter.font.Font(family = 'Arial', size=25, weight = 'bold')
            label5.grid(row=2,column=1)
            root.update()
   
            for x in range(side):
                for y in range(side):
                    if [x, y] not in hit and [x, y] not in miss:
                        l1[x][y].configure(bg='#22DFF7', state = NORMAL)
                    elif [x, y] in hit:
                        l1[x][y].configure(bg='red', state = DISABLED)
                    else:
                        l1[x][y].configure(bg='#0063FF', state = DISABLED)
            root.mainloop()

            chances += 1

            for x in range(side):
                for y in range(side):
                    l1[x][y].configure(state = DISABLED)

            #Computer Attacking system
            
            label5.grid_forget()         
            label5 = Label(root,text="Computer's Turn", fg = '#E20BCE')
            label5['font'] = tkinter.font.Font(family = 'Arial', size=25, weight = 'bold')
            label5.grid(row=2,column=1)
            root.update()
            time.sleep(1.2)

            done = False
            while done == False:#checks if chance is done
                if t == 0: #Random attacking
                    if easy == True:
                        while True:
                            a,b = random.randint(0,side-1),random.randint(0,side-1)
                            if [a,b] not in hit2 and [a,b] not in miss2:
                                break
                    else: ##### Difficult part <<<-------------------------------------####
                        direction = random.randint(0,1)
                        if direction == 0: #horizontal
                            while True:
                                a = random.randint(0,side-1)
                                possible = []
                                for b in range(side):
                                    if [a,b] not in hit2 and [a,b] not in miss2 and (hori_poss(a,b,len(ships2[-1])) or vert_poss(a,b,len(ships2[-1]))):
                                        possible.append(b)
                                if len(possible) == 1:
                                    b = possible[0]
                                    break
                                elif len(possible) == side:
                                    b = random.randint(0,9)
                                    break
                                elif len(possible) > 1:
                                    b = bestMove(a,possible,len(ships2[-1]),'hor')
                                    break
                        else: #vertical
                            while True:
                                b = random.randint(0,side-1)
                                possible = []
                                for a in range(side):
                                    if [a,b] not in hit2 and [a,b] not in miss2 and (hori_poss(a,b,len(ships2[-1])) or vert_poss(a,b,len(ships2[-1]))):
                                        possible.append(a)
                                if len(possible) == 1:
                                    a = possible[0]
                                    break
                                elif len(possible) == side:
                                    a = random.randint(0,9)
                                    break
                                elif len(possible) > 1:
                                    a = bestMove(b,possible,len(ships2[-1]),'ver')
                                    break
                    i = [a,b]
                    
                    if board2[a][b] != 'ship':
                        l2[a][b].configure(bg = '#0063FF')
                        miss2.append(i)
                        label3 = Label(root,text = "Miss",fg = 'blue')
                        label3['font'] = tkinter.font.Font(family = 'Arial', size=20)
                        label3.grid(row=3,column=2)
                        done = True
                    elif board2[a][b] == 'ship':
                        l2[a][b].configure(bg = 'red')
                        hit2.append(i)
                        score -= 10
                        label3 = Label(root,text = "Hit",fg = 'red')
                        label3['font'] = tkinter.font.Font(family = 'Arial', size=20)
                        label3.grid(row=3,column=2)
                        t = 1 #Makes it go into intelligent mode
                        d = 2
                        moves.append(i)
                        done = True
                else:
                    if d == 2: #condition req by later program, for checking if all moves in one line are finished
                        while True:
                            k = random.randint(1,2)
                            temp = random.randint(0,len(moves)-1) #helps to choose a random coordinate from moves[]
                            fix = moves[temp]#fix becomes starting point of intelligent firing
                            if k == 1 and hori_poss(fix[0],fix[1],len(ships2[-1])):
                                break
                            elif k == 2 and vert_poss(fix[0],fix[1],len(ships2[-1])):
                                break
                        pos = temp
                        d = 0
                    if k == 1: #horizontal
                        let = fix[0]
                        while True: 
                            num = random.randint(0,side-1)
                            if d == 0 and num == moves[pos][1] + 1: #moving right, here pos will keep changing after every move 
                                break
                            elif d == 0 and moves[pos][1] == side-1: #reached right boundary of grid
                                d = 1
                            elif d == 1 and num == moves[temp][1] - 1: #moving left
                                break
                            elif d == 1 and moves[temp][1] == 0: #reached left boundary of grid
                                d = 2
                            elif d == 2: #moves in line over
                                break
                        i = [let,num]
                        if d == 2: #moves over, skips all other conditions below
                            pass
                        elif board2[let][num] != 'ship' and i not in miss2: #miss
                            l2[let][num].configure(bg = '#0063FF')
                            miss2.append(i)
                            label3 = Label(root,text = "Miss",fg = 'blue')
                            label3['font'] = tkinter.font.Font(family = 'Arial', size=20)
                            label3.grid(row=3,column=2)
                            d += 1 #makes it move in other direction
                            done = True
                        elif i in miss2 or i in hit2: #this direction already blocked, go other way
                            d += 1 #without considering this a move
                        elif board2[let][num] == 'ship' and i not in hit2: #hit
                            l2[let][num].configure(bg = 'red')
                            hit2.append(i)
                            score -= 10
                            label3 = Label(root,text = "Hit",fg = 'red')
                            label3['font'] = tkinter.font.Font(family = 'Arial', size=20)
                            label3.grid(row=3,column=2)
                            if d == 0: #going right
                                pos += 1 #go to next position to insert coordinate
                                moves.insert(pos,i)
                            else:
                                moves.insert(temp,i)#ship keeps getting updated in correct order while going left by not changing temp
                            done = True
                            for z in range(len(ships2)):#to check if ship was destroyed when moving intelligently
                                for y in ships2[z]:
                                    flag = 1
                                    if y not in moves:
                                        flag = 0
                                        break
                                else:
                                    break
                            if flag == 1: #ship destroyed
                                d += 1 #change direction
                                if d == 1 and moves[temp+1] in ships2[z]: #may not be needed, helps to change direction to increase chance of hitting
                                        d += 1 #as ship in that line is completely destroyed, and the starting position may be of ship in other direction 
                                del(moves[moves.index(ships2[z][0]): moves.index(ships2[z][-1])+1])
                                for u in range(5):
                                    if ships2copy[u] == ships2[z]: #helps to get u which in turn helps to get the ship name as 4-u
                                        break
                                score -= 5
                                label4 = Label(root,text ='Your ' + shipName[4-u] + ' has been destroyed!')
                                label4['font'] = tkinter.font.Font(family = 'Arial', size=18)
                                label4.grid(row=4,column=2)
                                root.update()
                                time.sleep(2.5)
                                del(ships2[z])
                        if len(moves) == 0:
                            t = 0                                                         

                    else: #vertical
                        num = fix[1]
                        while True:
                            let = random.randint(0,side-1)
                            if d == 0 and let == moves[pos][0] + 1:
                                break
                            elif d == 0 and moves[pos][0] == side-1:
                                d = 1
                            elif d == 1 and let == moves[temp][0] - 1:
                                break
                            elif d == 1 and moves[temp][0] == 0:
                                d = 2
                            elif d == 2:
                                break
                        i = [let,num]
                        if d == 2: #moves over, skips all other conditions below
                            pass
                        elif board2[let][num] != 'ship' and i not in miss2: #miss
                            l2[let][num].configure(bg = '#0063FF')
                            miss2.append(i)
                            label3 = Label(root,text = "Miss",fg = 'blue')
                            label3['font'] = tkinter.font.Font(family = 'Arial', size=20)
                            label3.grid(row=3,column=2)
                            d += 1 #makes it move in other direction
                            done = True
                        elif i in miss2 or i in hit2: #this direction already blocked, go other way
                            d += 1 #without considering this a move
                        elif board2[let][num] == 'ship' and i not in hit2: #hit
                            l2[let][num].configure(bg = 'red')
                            hit2.append(i)
                            score -= 10
                            label3 = Label(root,text = "Hit",fg = 'red')
                            label3['font'] = tkinter.font.Font(family = 'Arial', size=20)
                            label3.grid(row=3,column=2)
                            if d == 0: #going right
                                pos += 1 #go to next position to insert coordinate
                                moves.insert(pos,i)
                            else:
                                moves.insert(temp,i)#ship keeps getting updated in correct order while going left by not changing temp
                            done = True
                            for z in range(len(ships2)):#to check if ship was destroyed when moving intelligently
                                for y in ships2[z]:
                                    flag = 1
                                    if y not in moves:
                                        flag = 0
                                        break
                                else:
                                    break
                            if flag == 1: #ship destroyed
                                d += 1 #change direction
                                if d == 1 and moves[temp+1] in ships2[z]: #may not be needed, helps to change direction to increase chance of hitting
                                        d += 1 #as ship in that line is completely destroyed, and the starting position may be of ship in other direction
                                del(moves[moves.index(ships2[z][0]): moves.index(ships2[z][-1])+1])
                                for u in range(5):
                                    if ships2copy[u] == ships2[z]: #helps to get u which in turn helps to get the ship name as 4-u
                                        break
                                score -= 5
                                label4 = Label(root,text ='Your ' + shipName[4-u] + ' has been destroyed!')
                                label4['font'] = tkinter.font.Font(family = 'Arial', size=18)
                                label4.grid(row=4,column=2)
                                root.update()
                                time.sleep(0.75)
                                del(ships2[z])
                        if len(moves) == 0:
                            t = 0

            root.update()
            time.sleep(1.5)

            label5.grid_forget()
            label2.grid_forget()
            label3.grid_forget()
            
            try:
                label1.grid_forget()
            except:
                pass

            try:
                label4.grid_forget()
            except:
                pass
            
            if ships == [[],[],[],[],[]] and len(ships2) == 0:
                win = True
                label5.grid_forget()
                label5 = Label(root,text="It's a Tie!\nWhat a coincidence!\n\nScore: " + str(score) + "\nChances: " + str(chances))
                label5['font'] = tkinter.font.Font(family = 'Verdana', size=20, weight = 'bold')
                label5.grid(row=2,column=1)
                break
            elif ships == [[],[],[],[],[]]:
                win = True
                label5.grid_forget()
                label5 = Label(root,text="You have Won!\nCongrats!\n\nScore: " + str(score) + "\nChances: " + str(chances))
                label5['font'] = tkinter.font.Font(family = 'Verdana', size=20, weight = 'bold')
                label5.grid(row=2,column=1)
                break
            elif len(ships2) == 0:
                win = False
                label5.grid_forget()
                label5 = Label(root,text="You have Lost!\nBetter luck next time\n\nScore: " + str(score) + "\nChances: " + str(chances))
                label5['font'] = tkinter.font.Font(family = 'Verdana', size=20, weight = 'bold')
                label5.grid(row=2,column=1)
                for x in range(5):
                    for y in range(len(ships[x])):
                        if ships[x][y] not in hit:
                            l1[ships[x][y][0]][ships[x][y][1]].configure(bg = '#AFAFAF')
                root.update()
                break

        Label(root).grid(row=5,column=1)
        Label(root).grid(row=6,column=1)
        Exit = Button(root,text = 'Exit', command = end, padx = 20)
        Exit['font'] = tkinter.font.Font(size = 30)
        Exit.grid(row=7,column=1)
        root.mainloop()
    except:
        pass

from tkinter import *
import tkinter.font as tkfont
import mysql.connector as sqLtor
import sys

from Pacman import game

interface = Tk()
interface.title('Arcade Games')
interface.state('zoomed')
interface.resizable(width = False, height = False)

interface.grid_columnconfigure(0, weight = 1) #Adjusts the size according to screen size, weight = 2 means size of column 0 increases twice as fast
interface.grid_rowconfigure(0, weight = 1)

def normal():
    global frame1,name,initial,check

    try:
        frame2.destroy()
    except:
        initial = ''

    frame1 = Frame(interface)
    frame1.grid(row=0,column=0)

    heading = Label(frame1,text = 'ARCADE GAMES 1.0', fg = 'red')
    heading['font'] = tkfont.Font(family = 'Jokerman', size=70, weight = 'bold')
    heading.grid(row = 0,column = 0, columnspan = 3)

    Label(frame1).grid(row=1,column = 0)

    lb1 = Label(frame1, text = 'Enter your name:', fg = 'green')
    lb1['font'] = tkfont.Font(family = 'Arial', size=30)
    lb1.grid(row = 2,column = 1)

    name = Entry(frame1,width = 40, justify = 'center')
    name['font'] = tkfont.Font(family = 'Arial', size=25)
    name.insert(0,initial) #inserts name back into field when you return to site
    name.grid(row = 3,column = 1)

    if check == 0:
        error = Label(frame1, text = '*Please enter your name first*', fg = 'red')
        error['font'] = tkfont.Font(size = 15)
        error.grid(row = 4, column = 1)
    elif check == 1:
        error = Label(frame1, text = '*Entered name is too long, please enter a shorter name*', fg = 'red')
        error['font'] = tkfont.Font(size = 15)
        error.grid(row = 4, column = 1)

    Label(frame1).grid(row=4,column = 0)
    Label(frame1).grid(row=5,column = 0)

    lb2 = Label(frame1, text = 'Choose a Game', fg = 'blue')
    lb2['font'] = tkfont.Font(family = 'Arial', size=55, weight = 'bold')
    lb2.grid(row = 6,column = 1)

    Label(frame1).grid(row=7,column = 0)

    game1 = Button(frame1, text = 'Battleship', fg = '#FF7000', command = batship)
    game1['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
    game1.grid(row = 8, column = 0)
    game2 = Button(frame1, text = 'Pac-Man', fg = '#FF7000', command = pacman_menu)
    game2['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
    game2.grid(row = 8, column = 2)

    Label(frame1).grid(row=9,column = 0)
    Label(frame1).grid(row=10,column = 0)

    Exit = Button(frame1, text = 'Exit', command = done)
    Exit['font'] = tkfont.Font(family = 'Arial', size=20)
    Exit.grid(row = 11, column = 1)
    interface.mainloop()

def batship():
    global check,initial,frame2
    try:
        frame2.destroy()
    except:
        pass

    try: #when you return to batship from inner menu, frame1 destroyed so name doesn't exist
        initial = name.get()
    except:
        pass
    if initial.strip() == '':
        check = 0
        frame1.destroy()
        normal()
    elif len(initial) > 40:
        check = 1
        frame1.destroy()
        normal()
    else:
        check = 2
        frame1.destroy()
        frame2 = Frame(interface)
        frame2.grid(row=0,column=0)

        heading = Label(frame2,text = 'Battleship', fg = 'red')
        heading['font'] = tkfont.Font(family = 'Jokerman', size=80, weight = 'bold')
        heading.grid(row = 0,column = 0, columnspan = 2)

        Label(frame2).grid(row=1,column = 0)

        play1 = Button(frame2,text = 'Play\n(Easy)', command = lambda: begin(True), fg = 'blue', padx = 20)
        play1['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
        play1.grid(row = 2, column = 0, padx = 100)

        play2 = Button(frame2,text = 'Play\n(Hard)', command = lambda: begin(False), fg = 'blue', padx = 20)
        play2['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
        play2.grid(row = 2, column = 1, padx = 100)

        Label(frame2).grid(row=3,column = 0)

        rules = Button(frame2,text = 'Rules', command = print_Rules, fg = 'Green')
        rules['font'] = tkfont.Font(family = 'Verdana', size=35, weight = 'bold')
        rules.grid(row = 4, column = 0, columnspan = 2)

        Label(frame2).grid(row=5,column = 0)

        high = Button(frame2,text = 'High Scores', command = show_Scores, fg = 'Yellow')
        high['font'] = tkfont.Font(family = 'Verdana', size=35, weight = 'bold')
        high.grid(row = 6, column = 0, columnspan = 2)

        Label(frame2).grid(row=7,column = 0,pady = 15)

        back = Button(frame2,text = 'Main Menu', command = normal)
        back['font'] = tkfont.Font(family = 'Arial', size=20)
        back.grid(row=8,column=0,columnspan = 2)

def pacman_menu():
    global check, initial, frame2
    try:
        frame2.destroy()
    except:
        pass

    try:
        initial = name.get()
    except:
        pass
    if initial.strip() == '':
        check = 0
        frame1.destroy()
        normal()
    elif len(initial) > 40:
        check = 1
        frame1.destroy()
        normal()
    else:
        check = 2
        frame1.destroy()
        frame2 = Frame(interface)
        frame2.grid(row=0, column=0)

        heading = Label(frame2, text='       Pac-man       ', fg='red')
        heading['font'] = tkfont.Font(family='Jokerman', size=80, weight='bold')
        heading.grid(row=0, column=0, columnspan=2)

        Label(frame2 ).grid(row=1, column=0)

        play1 = Button(frame2, text='Play', command=lambda: play_pacman(initial), fg='blue', padx=20)
        play1['font'] = tkfont.Font(family='Verdana', size=45, weight='bold')
        play1.grid(row=2, column=0, padx=100, columnspan=2)

        Label(frame2).grid(row=3, column=0)

        rules = Button(frame2, text='Instructions', command=rules_pacman, fg='Green')
        rules['font'] = tkfont.Font(family='Verdana', size=35, weight='bold')
        rules.grid(row=4, column=0)

        high = Button(frame2, text='High Scores', command=show_Scores_pac, fg='Yellow')
        high['font'] = tkfont.Font(family='Verdana', size=35, weight='bold')
        high.grid(row=4, column=1)

        Label(frame2).grid(row=7, column=0, pady=15)

        back = Button(frame2, text='Main Menu', command=normal)
        back['font'] = tkfont.Font(family='Arial', size=20)
        back.grid(row=8, column=0, columnspan=2)

def begin(easy):
    global initial
    interface.option_add("*font", tkfont.nametofont("TkDefaultFont")) #option_add adds the change to all the widgets that come after it.
    #nametofont accesses the font object and allows us to change it back to Default Font
    modules = list(sys.modules.keys()) #name of modules
    for mod in modules:
        if mod.startswith('Battleship.'):
            del(sys.modules[mod]) #so that game can be imported multiple times
    import Battleship.shared
    Battleship.shared.easy = easy #take the easy argument in a separate file to use in Attacking
    import Battleship.Attacking
    try:
        if Battleship.Attacking.win:
            results(initial, Battleship.Attacking.score, Battleship.Attacking.chances)
        initial = ''
        normal()
    except:
        pass

def play_pacman(name):
    global initial
    player_score = game.game()
    add_to_database(player_score, name)
    initial = ''
    normal()

def print_Rules():
    global frame2
    frame2.destroy()
    frame2 = Frame(interface)
    frame2.grid(row=0,column=0)

    interface.option_add("*font", "Arial 20")

    heading = Label(frame2,text = 'Battleship Rules', fg = 'red')
    heading['font'] = tkfont.Font(family = 'Jokerman', size=60, weight = 'bold')
    heading.grid(row = 0,column = 0, columnspan = 9, pady = 15)

    Label(frame2, text = "Find and destroy the computer's ships hidden on the board before it destroy's yours").grid(row = 1, column = 0, pady = 10, columnspan = 9)

    header1 = Label(frame2,text = 'Ships', fg = 'blue')
    header1['font'] = tkfont.Font(family = 'Verdana', size=30, weight = 'bold')
    header1.grid(row = 2,column = 0, columnspan = 9, pady = 15)

    frames = []
    shipNames = ['Aircraft Carrier','Battleship','Destroyer','Submarine','Patrol Boat']
    sizes = (5,4,3,3,2)

    for i in range(5):
        Label(frame2, text = shipNames[i]).grid(row = 3, column = i*2)
        frames.append(Frame(frame2))
        frames[-1].grid(row = 4, column = i*2)
        for j in range(sizes[i]):
            Button(frames[-1], padx=19, pady=9, state = DISABLED, bg='#AFAFAF').grid(row = 0, column = j)
            Label(frame2).grid(row = 4, column = i*2 + 1, padx = 5)#change
    Label(frame2).grid(row = 4, column = 1, padx = 40)
    Label(frame2).grid(row = 4, column = 3, padx = 40)
    Label(frame2).grid(row = 4, column = 5, padx = 40)
    Label(frame2).grid(row = 4, column = 7, padx = 40)

    RuleFrame = Frame(frame2)
    RuleFrame.grid(row = 5,column = 0, columnspan = 9, pady = 35)

    defense = Button(RuleFrame,text = 'Defense',fg='blue', command = print_Rules_Defense)
    defense['font'] = tkfont.Font(family = 'Verdana', size=25, weight = 'bold')
    defense.grid(row=0,column=0,padx = 60)

    attack = Button(RuleFrame,text = 'Attack',fg='blue', command = print_Rules_Attack, padx = 15)
    attack['font'] = tkfont.Font(family = 'Verdana', size=25, weight = 'bold')
    attack.grid(row=0,column=1,padx = 60)

    scoring = Button(RuleFrame,text = 'Scoring',fg='blue', command = print_Rules_Scoring)
    scoring['font'] = tkfont.Font(family = 'Verdana', size=25, weight = 'bold')
    scoring.grid(row=0,column=2,padx = 60)

    back = Button(frame2,text = 'Back', command = batship)
    back['font'] = tkfont.Font(family = 'Arial', size=20)
    back.grid(row=6,column=0, columnspan = 9)

def print_Rules_Defense():
    global frame2
    frame2.destroy()
    frame2 = Frame(interface)
    frame2.grid(row=0,column=0)

    interface.option_add("*font", "Arial 15")

    header1 = Label(frame2,text = 'Defense', fg = 'blue')
    header1['font'] = tkfont.Font(family = 'Verdana', size=30, weight = 'bold')
    header1.grid(row = 0,column = 0, columnspan = 3, pady = 15)

    Label(frame2, text = "First you must set up your own board by placing your ships.\n\n\
You can place your ships horizontally or vertically on the board by clicking on one of the blue squares.\n\n\
Selected squares will turn grey in colour and will prompt you to choose your orientation with the white squares.\n\n\
You cannot place a ship diagonally or over another ship.\n\n\
Places which you cannot select will be deactivated.", wraplength = 1300).grid(row = 1, column = 0, columnspan = 3)

    frameA = Frame(frame2)
    frameA.grid(row = 2, column = 0, pady = 10)
    frameB = Frame(frame2)
    frameB.grid(row = 2, column = 1)
    frameC = Frame(frame2)
    frameC.grid(row = 2, column = 2)

    l = []
    for x in range(5):
        k = []
        for y in range(5):
            k.append(Button(frameA, padx=18, pady=10, state = DISABLED, bg='#22DFF7'))
            k[y].grid(row=x, column=y)
        l.append(k)
    l = []
    for x in range(5):
        k = []
        for y in range(5):
            k.append(Button(frameB, padx=18, pady=10, state = DISABLED, bg='#22DFF7'))
            k[y].grid(row=x, column=y)
        l.append(k)
    l[0][1].configure(bg = 'white')
    l[0][2].configure(bg = '#767676')
    l[0][3].configure(bg = 'white')
    l[1][2].configure(bg = 'white')
    l = []
    for x in range(5):
        k = []
        for y in range(5):
            k.append(Button(frameC, padx=18, pady=10, state = DISABLED, bg='#22DFF7'))
            k[y].grid(row=x, column=y)
        l.append(k)
    l[0][2].configure(bg = '#AFAFAF')
    l[0][3].configure(bg = '#AFAFAF')
    l[0][4].configure(bg = '#AFAFAF')
    l[1][1].configure(bg = 'white')
    l[2][1].configure(bg = '#767676')
    l[3][1].configure(bg = '#767676')
    l[4][1].configure(bg = 'white')

    Label(frame2, text = "Once placed, you can confirm your board to begin the game.").grid(row = 3, column = 0, columnspan = 3, pady = 10)

    back = Button(frame2,text = 'Back', command = print_Rules)
    back['font'] = tkfont.Font(family = 'Arial', size=20)
    back.grid(row=4,column=0, columnspan = 3)

def print_Rules_Attack():
    global frame2
    frame2.destroy()
    frame2 = Frame(interface)
    frame2.grid(row=0,column=0)

    interface.option_add("*font", "Arial 15")

    header1 = Label(frame2,text = 'Attack', fg = 'blue')
    header1['font'] = tkfont.Font(family = 'Verdana', size=30, weight = 'bold')
    header1.grid(row = 0,column = 0, columnspan = 3, pady = 15)

    Label(frame2, text = "Once the game begins, you and the computer will turn by turn try to guess where the other's ships are placed.\n\n\
You must try to find the computer's ships by clicking on the light blue coloured squares on your Attack Board (On the left).\n\n\
The computer also keeps attacking your ships which you can track on your Defense Board (On the right).\n\n\
If you find a ship, it displays the hit with a red colour.\n\n\
If you miss the ship, it displays a dark blue colour.\n\n\
The computer informs you of every move at the bottom of the boards\n\n\
It will also send you updates of the destruction of any ship", wraplength = 1300).grid(row = 1, column = 0, columnspan = 3)

    frameA = Frame(frame2)
    frameA.grid(row = 2, column = 0, pady = 10)
    frameB = Frame(frame2)
    frameB.grid(row = 2, column = 1)
    frameC = Frame(frame2)
    frameC.grid(row = 2, column = 2)

    l = []
    for x in range(5):
        k = []
        for y in range(5):
            k.append(Button(frameA, padx=18, pady=10, state = DISABLED, bg='#22DFF7'))
            k[y].grid(row=x, column=y)
        l.append(k)
    l = []
    for x in range(5):
        k = []
        for y in range(5):
            k.append(Button(frameB, padx=18, pady=10, state = DISABLED, bg='#22DFF7'))
            k[y].grid(row=x, column=y)
        l.append(k)
    l[1][0].configure(bg = 'red')
    l[4][1].configure(bg = 'blue')
    l[2][0].configure(bg = 'blue')
    l[1][4].configure(bg = 'blue')
    l[2][3].configure(bg = 'blue')
    l = []
    for x in range(5):
        k = []
        for y in range(5):
            k.append(Button(frameC, padx=18, pady=10, state = DISABLED, bg='#22DFF7'))
            k[y].grid(row=x, column=y)
        l.append(k)
    l[0][0].configure(bg = 'red')
    l[1][0].configure(bg = 'red')
    l[3][1].configure(bg = 'red')
    l[3][2].configure(bg = 'red')
    l[3][3].configure(bg = 'red')
    l[3][4].configure(bg = 'red')
    l[4][1].configure(bg = 'blue')
    l[2][0].configure(bg = 'blue')
    l[0][2].configure(bg = 'blue')
    l[1][4].configure(bg = 'blue')
    l[2][3].configure(bg = 'blue')

    back = Button(frame2,text = 'Back', command = print_Rules)
    back['font'] = tkfont.Font(family = 'Arial', size=20)
    back.grid(row=3,column=0, columnspan = 3)

def print_Rules_Scoring():
    global frame2
    frame2.destroy()
    frame2 = Frame(interface)
    frame2.grid(row=0,column=0)

    interface.option_add("*font", "Arial 18")

    header1 = Label(frame2,text = 'Scoring', fg = 'blue')
    header1['font'] = tkfont.Font(family = 'Verdana', size=30, weight = 'bold')
    header1.grid(row = 0,column = 0, columnspan = 3, pady = 35)

    Label(frame2, text = "If you hit the computer's ship, you get 20 points\n\n\
If you destroy an entire ship, you get an additional 10 points\n\n\
If the computer gets a hit on your ship, you lose 10 points\n\n\
If the computer destroys an entire ship, you lose an additional 5 points\n\n\
The number of moves you took to complete the game also adds to your score", wraplength = 1300).grid(row = 1, column = 0, columnspan = 3)

    Label(frame2).grid(row=2,column=0)
    Label(frame2).grid(row=3,column=0)
    Label(frame2).grid(row=4,column=0)
    back = Button(frame2,text = 'Back', command = print_Rules)
    back['font'] = tkfont.Font(family = 'Arial', size=20)
    back.grid(row=5,column=0, columnspan = 3)

def rules_pacman():
    global frame2
    frame2.destroy()
    frame2 = Frame(interface)
    frame2.grid(row=0, column=0)

    interface.option_add("*font", "Arial 20")

    heading = Label(frame2, text='How to play', fg='red')
    heading['font'] = tkfont.Font(family='Jokerman', size=60, weight='bold')
    heading.grid(row=0, column=0, pady=15)

    Label(frame2, text="Use the arrow keys to control pacman").grid(row=1, column=0, pady=10)
    Label(frame2, text="Eat all the small pellets to clear the level").grid(row=2, column=0, pady=10)
    Label(frame2, text="Once you eat a big pellet you can eat ghosts for points while they are frightened").grid(row=3, column=0, pady=10)

    header1 = Label(frame2, text='Don\'t get caught by the ghosts!', fg='blue')
    header1['font'] = tkfont.Font(family='Verdana', size=30, weight='bold')
    header1.grid(row=4, column=0, pady=15)

    back = Button(frame2, text='Back', command=pacman_menu)
    back['font'] = tkfont.Font(family='Arial', size=20)
    back.grid(row=6, column=0)

def results(name, score, chances):
    global cursor, mycon
    cursor.execute('INSERT INTO Battleship_Scores VALUES("{0}", {1}, {2})'.format(name, score, chances))
    cursor.execute('INSERT INTO Battleship_Chances VALUES("{0}", {1}, {2})'.format(name, chances, score))
    mycon.commit()
    cursor.execute('SELECT * FROM Battleship_Scores ORDER BY score DESC, chances ASC')
    data = cursor.fetchall()
    if len(data) > 5:
        cursor.execute('DELETE FROM Battleship_Scores WHERE username = "{0}" AND score = {1} AND chances = {2}'.format(data[5][0],data[5][1],data[5][2]))
        mycon.commit()
    cursor.execute('SELECT * FROM Battleship_Chances ORDER BY chances ASC, score DESC')
    data = cursor.fetchall()
    if len(data) > 5:
        cursor.execute('DELETE FROM Battleship_Chances WHERE username = "{0}" AND chances = {1} AND score = {2}'.format(data[5][0],data[5][1],data[5][2]))
        mycon.commit()

def show_Scores():
    global frame2, mycon, cursor
    mycon.close()
    mycon = sqLtor.connect(host='localhost', user='root', passwd=pwd)
    cursor = mycon.cursor()
    cursor.execute('USE scores')
    frame2.destroy()
    frame2 = Frame(interface)
    frame2.grid(row=0,column=0)
    interface.option_add("*font", "Arial 15")

    heading1 = Label(frame2,text = 'Best Scores', fg = 'red')
    heading1['font'] = tkfont.Font(family = 'Jokerman', size=50, weight = 'bold')
    heading1.grid(row = 0,column = 0, columnspan = 2)

    username1 = Label(frame2,text = 'Username', fg = 'blue')
    username1['font'] = tkfont.Font(family = 'Arial', size=20, weight = 'bold')
    username1.grid(row = 1,column = 0, pady = 20, padx = 20)

    score1 = Label(frame2,text = 'Score', fg = 'blue')
    score1['font'] = tkfont.Font(family = 'Arial', size=20, weight = 'bold')
    score1.grid(row = 1,column = 1)

    cursor.execute('SELECT * FROM Battleship_Scores ORDER BY score DESC, chances ASC')
    data = cursor.fetchall()

    for i in range(len(data)):
        Label(frame2, text = data[i][0]).grid(row = i+2, column = 0)
        Label(frame2, text = data[i][1]).grid(row = i+2, column = 1)

    if len(data) == 0:
        Label(frame2, text = 'No Highscores Yet').grid(row = 2, column = 0, columnspan = 2)
        i = 0

    heading2 = Label(frame2,text = 'Quickest Games', fg = 'red')
    heading2['font'] = tkfont.Font(family = 'Jokerman', size=50, weight = 'bold')
    heading2.grid(row = 3+i,column = 0, columnspan = 2)

    username2 = Label(frame2,text = 'Username', fg = 'blue')
    username2['font'] = tkfont.Font(family = 'Arial', size=20, weight = 'bold')
    username2.grid(row = 4+i,column = 0, pady = 20)

    chances2 = Label(frame2,text = 'Chances', fg = 'blue')
    chances2['font'] = tkfont.Font(family = 'Arial', size=20, weight = 'bold')
    chances2.grid(row = 4+i,column = 1)

    cursor.execute('SELECT * FROM Battleship_Chances ORDER BY chances ASC, score DESC')
    data = cursor.fetchall()

    for j in range(len(data)):
        Label(frame2, text = data[j][0]).grid(row = 5+i+j, column = 0)
        Label(frame2, text = data[j][1]).grid(row = 5+i+j, column = 1)

    if len(data) == 0:
        Label(frame2, text = 'No Highscores Yet').grid(row = 5+i, column = 0, columnspan = 2)
        j = 0

    back = Button(frame2,text = 'Back', command = batship)
    back['font'] = tkfont.Font(family = 'Arial', size=20)
    back.grid(row=6+i+j,column=0, columnspan = 2, pady = 20)

def add_to_database(score, username):
    global cursor, mycon
    cursor.execute('INSERT INTO pacman_scores VALUES("{0}", {1})'.format(username, score))
    mycon.commit()

    cursor.execute('SELECT * FROM pacman_scores ORDER BY score DESC')
    data = cursor.fetchall()
    if len(data) > 10:
        cursor.execute('DELETE FROM pacman_scores WHERE username = "{0}" AND score = {1}'.format(data[10][0],data[10][1]))
        mycon.commit()

def show_Scores_pac():
    global frame2, mycon, cursor
    
    frame2.destroy()
    frame2 = Frame(interface)
    frame2.grid(row=0,column=0)
    interface.option_add("*font", "Arial 15")

    heading1 = Label(frame2,text = 'Best Scores', fg = 'red')
    heading1['font'] = tkfont.Font(family = 'Jokerman', size=50, weight = 'bold')
    heading1.grid(row = 0,column = 0, columnspan = 2)

    username1 = Label(frame2,text = 'Username', fg = 'blue')
    username1['font'] = tkfont.Font(family = 'Arial', size=20, weight = 'bold')
    username1.grid(row = 1,column = 0, pady = 20, padx = 20)

    score1 = Label(frame2,text = 'Score', fg = 'blue')
    score1['font'] = tkfont.Font(family = 'Arial', size=20, weight = 'bold')
    score1.grid(row = 1,column = 1)

    cursor.execute('SELECT * FROM pacman_scores ORDER BY score DESC')
    data = cursor.fetchall()

    for i in range(len(data)):
        Label(frame2, text = data[i][0]).grid(row = i+2, column = 0)
        Label(frame2, text = data[i][1]).grid(row = i+2, column = 1)

    if len(data) == 0:
        Label(frame2, text = 'No Highscores Yet').grid(row = 2, column = 0, columnspan = 2)
        i = 0

    back = Button(frame2,text = 'Back', command = pacman_menu)
    back['font'] = tkfont.Font(family = 'Arial', size=20)
    back.grid(row=6+i,column=0, columnspan = 2, pady = 20)

def done():
    interface.destroy()

# Database code
pwd = '1234'  # Change this for it to work

mycon = sqLtor.connect(host='localhost', user='root', passwd=pwd)
cursor = mycon.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS scores')
cursor.execute('USE scores')
cursor.execute('CREATE TABLE IF NOT EXISTS Battleship_Scores(username varchar(40), score int, chances int)')
cursor.execute('CREATE TABLE IF NOT EXISTS Battleship_Chances(username varchar(40), chances int, score int)')
cursor.execute('CREATE TABLE IF NOT EXISTS pacman_scores(username varchar(40), score int)')

check = 2
normal()

mycon.close()

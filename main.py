# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 23:10:06 2023

@author: Mansoor
"""

from tkinter import *

# Environment setup
tk = Tk()
tk.geometry('340x560')
tk.title('Tic Tac Toe')

# Board setup
board = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

# Logic setup
turn = "X"
gameOver = False
mode = 'singlePlayer'


#function to check winner
def checkforwin(player):
    if board[1] == board[2] == board[3] == player:
        return True
    elif board[4] == board[5] == board[6] == player:
        return True
    elif board[7] == board[8] == board[9] == player:
        return True
    elif board[1] == board[4] == board[7] == player:
        return True
    elif board[2] == board[5] == board[8] == player:
        return True
    elif board[3] == board[6] == board[9] == player:
        return True
    elif board[1] == board[5] == board[9] == player:
        return True
    elif board[3] == board[5] == board[7] == player:
        return True
    return False

def ismatchdraw():
    for i in board.keys():
        if board[i] == '':
            return False
    return True
#function for computer or player turn
def changeModeSingle():
    global mode
    mode = "singlePlayer"
    restartGame()
    singleplayer['fg'] = 'black'
    singleplayer['bg'] = 'white'
    multiplayer['fg'] = 'white'
    multiplayer['bg'] = 'black'

        
def changeModeMulti():
    global mode
    mode = "multiPlayer"
    restartGame()
    multiplayer['fg'] = 'black'
    multiplayer['bg'] = 'white'
    singleplayer['fg'] = 'white'
    singleplayer['bg'] = 'black'

    
def restartGame():
    for button in buttons:
        button['text'] = ''

    for i in board.keys():
        board[i] = ''

    global gameOver,turn
    turn = 'X'
    gameOver = False
    
    playerturn['text'] = 'Tic Toc Toe'
    playerturn['fg'] = 'black'
    playerturn['bg'] = 'gray'
    restart['bg'] = 'gray'
    restart['fg'] = 'black'
    multiplayer['bg'] = 'black'
    multiplayer['fg'] = 'white'
    singleplayer['bg'] = 'black'
    singleplayer['fg'] = 'white'


def minmax(board, isMaximize):
    if checkforwin('O'):
        return 1
    elif checkforwin('X'):
        return -1
    elif ismatchdraw():
        return 0

    if isMaximize:
        bestScore = -10
        for key in board.keys():
            if board[key] == '':
                board[key] = 'O'
                score = minmax(board, False)
                board[key] = ''
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 10
        for key in board.keys():
            if board[key] == '':
                board[key] = 'X'
                score = minmax(board, True)
                board[key] = ''
                bestScore = min(score, bestScore)
        return bestScore

def computerPlay():
    bestScore = -10
    bestMove = 0
    for key in board.keys():
        if board[key] == '':
            board[key] = 'O'
            score = minmax(board, False)
            board[key] = ''
            if score > bestScore:
                bestScore = score
                bestMove = key

    board[bestMove] = 'O'
    buttons[bestMove-1]['text'] = 'O'



def playUser(event):
    global turn, gameOver
    if gameOver:
        return

    button = event.widget

    boardposition = str(button)[-1]
    if boardposition=='n':
        boardposition = 1
    else:
        boardposition = int(boardposition)
        
    if board[boardposition] == '':
        if turn == 'X':
            button['text'] = 'X'
            board[boardposition] = 'X'
            checkvalidity(turn)
            turn = 'O'
            if mode=='singlePlayer':  
            #run computer function to give him its turn
                computerPlay()
                checkvalidity(turn)
                turn = 'X'    
        else:
            button['text'] = 'O'
            board[boardposition] = 'O'
            checkvalidity(turn)
            turn = 'X'
            
def checkvalidity(player):
    if checkforwin(turn):
        playerturn['text'] = f'{turn}-Won'
        playerturn['fg'] = 'red'
        playerturn['bg'] = 'black'
        restart['fg'] = 'red'
        restart['bg'] = 'black'
        gameOver = True
    
    elif ismatchdraw():
        playerturn['text'] = 'Match Draw'
        playerturn['fg'] = 'orange'
        restart['fg'] = 'orange'
    

    
#GUI Setup

#first frame for player turn
frame1 = Frame(tk)
frame1.pack()
 
playerturn = Button(frame1,text='Tic Toc Toe',font=('Times New Roman',20),fg='black',bg='gray',relief= RAISED,borderwidth=7,width=20,height=0)
playerturn.grid(row=0,column=0)

#second frame for player mode
frame2 = Frame(tk)
frame2.pack()
 
singleplayer = Button(frame2,text='Single Player',font=('Times New Roman',10),fg='white',bg='black',relief= RAISED,borderwidth=8,width=20,height=1,command=changeModeSingle)
singleplayer.grid(row=0,column=0,sticky=NW)


multiplayer = Button(frame2,text='Multi Player',font=('Times New Roman',10),fg='white',bg='black',relief= RAISED,borderwidth=8,width=20,height=1,command=changeModeMulti)
multiplayer.grid(row=0,column=1,sticky=NW)


#Third frame for buttons
frame3 = Frame(tk)
frame3.pack()

#first row button 
button1 = Button(frame3,text='',font=('Arial',30),fg='white',bg='black',relief= RAISED,borderwidth=5,width=4,height=2)
button1.grid(row=0,column=0)
button1.bind('<Button-1>',playUser)

button2 = Button(frame3,text='',font=('Arial',30),fg='white',bg='black',relief= RAISED,borderwidth=5,width=4,height=2)
button2.grid(row=0,column=1)
button2.bind('<Button-1>',playUser)

button3 = Button(frame3,text='',font=('Arial',30),fg='white',bg='black',relief= RAISED,borderwidth=5,width=4,height=2)
button3.grid(row=0,column=2)
button3.bind('<Button-1>',playUser)

#second row button
button4 = Button(frame3,text='',font=('Arial',30),fg='white',bg='black',relief= RAISED,borderwidth=5,width=4,height=2)
button4.grid(row=1,column=0)
button4.bind('<Button-1>',playUser)

button5 = Button(frame3,text='',font=('Arial',30),fg='white',bg='black',relief= RAISED,borderwidth=5,width=4,height=2)
button5.grid(row=1,column=1)
button5.bind('<Button-1>',playUser)

button6 = Button(frame3,text='',font=('Arial',30),fg='white',bg='black',relief= RAISED,borderwidth=5,width=4,height=2)
button6.grid(row=1,column=2)
button6.bind('<Button-1>',playUser)

#third row button
button7 = Button(frame3,text='',font=('Arial',30),fg='white',bg='black',relief= RAISED,borderwidth=5,width=4,height=2)
button7.grid(row=2,column=0)
button7.bind('<Button-1>',playUser)

button8 = Button(frame3,text='',font=('Arial',30),fg='white',bg='black',relief= RAISED,borderwidth=5,width=4,height=2)
button8.grid(row=2,column=1)
button8.bind('<Button-1>',playUser)

button9 = Button(frame3,text='',font=('Arial',30),fg='white',bg='black',relief= RAISED,borderwidth=5,width=4,height=2)
button9.grid(row=2,column=2)
button9.bind('<Button-1>',playUser)

#third frame for restart button 
frame4 = Frame(tk)
frame4.pack()
 
restart = Button(frame4,text='Restart',font=('Times New Roman',20),fg='black',bg='gray',relief= RAISED,borderwidth=7,width=20,height=0,command=restartGame)
restart.grid(row=0,column=0)

#list of our buttons
buttons = [button1,button2,button3,button4,button5,button6,button7,button8,button9]

tk.mainloop()
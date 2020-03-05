from tkinter import *

from math import inf
from random import choice
import time


board = (' ',) * 9


def set_pos(i, p):
    return board[:i] + (p,) + board[i + 1:]


def get_empty(b):
    return [i for i in range(len(b)) if b[i] == ' ']


def minimax(state, depth, player):
    if player == 'O':
        best = [-1, -inf]
    else:
        best = [-1, inf]

    if depth == 0 or check_winner(board) in ['X', 'O']:
        score = check_winner(state)
        return [-1, score]

    for index in get_empty(state):
        print(state, 'state - before')
        state = state[:index] + (player, ) + state[index + 1:]
        score = minimax(state, depth - 1, ('O', 'X')[player == 'O'])
#        state[index] = 0
        score[0] = index
        print(state, 'state - after')
        print(score, 'score')
        print(best, 'best')
        if player == 'O':
            if score[0] > best[0]:
                print(best, score)
                best[0] = score[0]  # max value
        else:
            if score[0] < best[0]:
                best[0] = score[0]  # min value

    return best


def ai_turn():
    depth = len(get_empty(board[:]))
    if depth == 0 or check_winner(board) in ['X', 'O']:
        return

    move = choice(get_empty(board)) if depth == 9 else minimax(board, depth, 'O')

    set_pos(move, 'O')
    time.sleep(1)


def listener(r, c):
    global player, board
    if button[r][c].cget('text') == ' ':
        button[r][c].configure(text=player)

        p = 3 * r + c
        board = board[:p] + (player, ) + board[p + 1:]

        player = 'X' if player == 'O' else 'O'
        w = check_winner(board)
        if w == 'X':
            print('X wins')
        elif w == 'O':
            print('O Wins')
        elif w == 'D':
            print('Draw')
    if player == 'O':
        ai_turn()


def check_winner(B):
    if B[0] == B[1] == B[2] != ' ':
        return B[0]
    if B[3] == B[4] == B[5] != ' ':
        return B[3]
    if B[6] == B[7] == B[8] != ' ':
        return B[6]

    if B[0] == B[3] == B[6] != ' ':
        return B[0]
    if B[1] == B[4] == B[7] != ' ':
        return B[1]
    if B[2] == B[5] == B[8] != ' ':
        return B[2]

    if B[0] == B[4] == B[8] != ' ':
        return B[0]
    if B[2] == B[4] == B[6] != ' ':
        return B[2]

    if B.count(' ') == 0:
        return 'D'

    return 'N'


root = Tk()
root.title('Tic-Tac-Toe')

button = [[0]*3 for i in range(3)]
for r in range(3):
    for c in range(3):
        B = Button(text=' ', font=('Courier New', 72), bg='#ffffff', command=lambda r=r, c=c:listener(r, c))
        B.grid(row=r, column=c)
        button[r][c] = B

player = 'X'

mainloop()


'''
# Game over message
if wins(board, HUMAN):
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)
    print('YOU WIN!')
elif wins(board, COMP):
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)
    print('YOU LOSE!')
else:
    render(board, c_choice, h_choice)
    print('DRAW!')
'''
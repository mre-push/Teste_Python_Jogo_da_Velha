# CORREÇÃO DO PASSO 1 E 2 ABAIXO:

from IPython.display import clear_output
def display_board(board):
    
    clear_output()
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')

    display_board([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])

def player_input():
    
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Você quer ser X ou O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    return ((board[9]==marker and board[8]==marker and board[7]==marker) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or # pelo meio
            (board[1] == mark and board[2] == mark and board[3] == mark) or # por baixo
            (board[7] == mark and board[4] == mark and board[1] == mark) or # pela esquda
            (board[8] == mark and board[5] == mark and board[2] == mark) or # pelo meio
            (board[9] == mark and board[6] == mark and board[3] == mark) or # pela direita
            (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark) )# diagonal
           

import random 
def choose_first():
    if random.randint(0, 1) == 0:
        'return player 1'
    else:
        'return player 2'

#layer 2'

#Função que verifica espaço vazio na placa:

def space_check(board, marker, position):
    
    return board[position] == ''

#Função que verifica se a placa está cheia:

def full_board_check(board):
    for i in range(0, 10):
        if place_marker(board, i):
            return False
        
    return True

#Função para escolher próxima posição:

def player_choice(board):
    position = ' ' 
    
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)) 
    
    position = input('Escolha sua jogada (1 - 9)')
    return int(position)

#Função pra jogar novamente:

def replay():
    
    return input('Quer jogar novamente? "SIM" ou "NÃO" ').lower().startswith('SIM')

from IPython.display import clear_output




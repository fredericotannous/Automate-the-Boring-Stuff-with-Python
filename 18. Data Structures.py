cat = {'name': 'zophie', 'age': 7, 'color': 'gray'}
allCats = []

allCats.append({'name': 'zophie', 'age': 7, 'color': 'gray'})
allCats.append({'name': 'kibe', 'age': 3, 'color': 'brown'})
allCats.append({'name': 'nina', 'age': 5, 'color': 'gold'})

print(allCats)

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' ' }

import pprint

theBoard['mid-M'] = 'X'
theBoard['top-M'] = 'O'
theBoard['top-R'] = 'O'
theBoard['mid-L'] = 'X'
theBoard['low-R'] = 'X'
theBoard['top-L'] = 'O'
pprint.pprint(theBoard)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----') 
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----') 
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)

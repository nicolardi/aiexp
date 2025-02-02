'''
8-Puzzle 
'''

from random import randrange, shuffle
import copy

puzzle = None

def randomPosition():
    # decido dove è la casellina bianca
    i=randrange(3)
    j=randrange(3)
    return (i,j)

def createRandomPuzzle():
    puzzle = [
        ['','',''],
        ['','',''],
        ['','','']
    ]
    (ei,ej) = randomPosition()
    orderedArray = list(range(1,10)) # la casella 9 diventerà bianca
    randomArray = orderedArray
    shuffle(randomArray)
    
    for index in range(0,9):
        (i,j) = (int(index / 3), index % 3)
        puzzle[i][j] = ' ' if randomArray[index] == 9 else randomArray[index]
    return puzzle    

def printPuzzle(puzzle):
    for i in range(0,3):
        for j in range(0,3):
            print(f'{puzzle[i][j]} ', end='')
        if i < 2:
            print()
    print('\n-----')
    
def findEmpty(puzzle):
    for i in range(0,3):
        for j in range(0,3):
            if (puzzle[i][j] == ' '):
                return (i,j)
    
def hashPuzzle(puzzle):
    hash = ''
    for i in range(0,3):
        for j in range(0,3):
            hash = hash + str(puzzle[i][j])
    return hash
    
def nextPossiblePuzzles(puzzle, ie, je, history):
    possiblePuzzles = []
    # movimento a sx
    
    if je > 0:
        new_puzzle = copy.deepcopy(puzzle)
        new_puzzle[ie][je] = puzzle[ie][je-1] 
        new_puzzle[ie][je-1] = ' ';
        hash = hashPuzzle(new_puzzle);
        if ( hash not in history):
            possiblePuzzles.append(new_puzzle)
            history.add(hash)
    # movimento a dx
    
    if (je <2):
        new_puzzle = copy.deepcopy(puzzle)
        new_puzzle[ie][je] = puzzle[ie][je+1] 
        new_puzzle[ie][je+1] = ' ';
        hash = hashPuzzle(new_puzzle);
        if ( hash not in history):
            possiblePuzzles.append(new_puzzle)
            history.add(hash)
    
    # movimento sopra
    if (ie >0):
        new_puzzle = copy.deepcopy(puzzle)
        new_puzzle[ie][je] = puzzle[ie-1][je] 
        new_puzzle[ie-1][je] = ' ';
        hash = hashPuzzle(new_puzzle);
        if ( hash not in history):
            possiblePuzzles.append(new_puzzle)
            history.add(hash)
            
    # movimento sotto
    if (ie <2):
        new_puzzle = copy.deepcopy(puzzle)
        new_puzzle[ie][je] = puzzle[ie+1][je] 
        new_puzzle[ie+1][je] = ' ';
        hash = hashPuzzle(new_puzzle);
        if ( hash not in history):
            possiblePuzzles.append(new_puzzle)
            history.add(hash)
    return possiblePuzzles


def solvedPuzzle(puzzle):
    return hashPuzzle(puzzle) == '12345678 '
    
def generateAllPossibleMoves(puzzles):
    history = set()
    moves = []
    safety = -1
    while len(puzzles) >0:
        puzzle = puzzles[0]
        if safety == 0:
            break
        safety = safety - 1    
        (ie, je) = findEmpty(puzzle)
        
        next_puzzles = nextPossiblePuzzles(puzzle, ie, je, history)
        # test if we have found the solution
        for p in next_puzzles:
            if solvedPuzzle(p):
                print(f"RISOLTO in {len(moves)}!!!")
                moves.append(p)
                printPuzzle(p);
                return []
                return moves
              
        moves.append(puzzle)
        puzzles.remove(puzzle)
        puzzles = puzzles + next_puzzles
        
    return moves
    
puzzle = createRandomPuzzle()

moves = generateAllPossibleMoves([puzzle])
'''
print(f'moves found: {len(moves)}')
for puzzle in moves:
    printPuzzle(puzzle)
'''
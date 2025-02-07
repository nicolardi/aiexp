'''
8-Puzzle 
'''

from random import randrange, shuffle
import copy
from tree import Tree

MAX_ITERATIONS = 100000
'''
puzzle = [
        [7,1,2],
        [8,4, 3],
        [' ',6,5]
    ]
'''

def generateRandomPuzzle():
    randomArray = ['0','1','2','3','4','5','6','7','8']
    shuffle(randomArray)
    return ''.join(randomArray) 

def printPuzzle(puzzle):
    print('---------')
    for i in range(9):
        print(f' {puzzle[i]} ', end='')
        if (i-2) % 3 == 0:
            print()
    print('---------')
        
def possibleMoves(puzzle, past_moves):
    i = puzzle.find('0')
    nextPuzzles = []

    # movimento a sx: pozizioni 1,2,4,5,7,8
    if i == 1 or i == 2 or i == 4 or i == 5 or i == 7 or i == 8:
       arr = list(puzzle)
       arr[i] = arr[i-1]
       arr[i-1] = '0'
       if ( "".join(arr) not in past_moves):
            nextPuzzles.append("".join(arr))

    # movimento dx: posizioni 0,1,3,4,6,7
    if i == 0 or i == 1 or i == 3 or i == 4 or i == 6 or i == 7:
       arr = list(puzzle)
       arr[i] = arr[i+1]
       arr[i+1] = '0'
       if ( "".join(arr) not in past_moves):
            nextPuzzles.append("".join(arr))
    
    # movimento up: posizioni 3,6,4,7,5,8
    if i == 3 or i == 6 or i == 4 or i == 7 or i == 5 or i == 8:
       arr = list(puzzle)
       arr[i] = arr[i-3]
       arr[i-3] = '0'
       if ( "".join(arr) not in past_moves):
            nextPuzzles.append("".join(arr))

    # movimento down: posizioni 0,1,2,3,4,5
    if i  <= 5:
       arr = list(puzzle)
       arr[i] = arr[i+3]
       arr[i+3] = '0'
       if ( "".join(arr) not in past_moves):
            nextPuzzles.append("".join(arr))
    return nextPuzzles
    
def addChild(puzzles, child, search_algorithm):
    if search_algorithm == 'depth_first_search':
        puzzles.append(child) # depth first search
    elif search_algorithm == 'breadth_first_search':
        puzzles.insert(0, child) # Breedth first search
    else:
        print(f'Search algorithm {search_algorithm} not implemented')
    exit

def getChild(puzzles):
    return puzzles[0]

def sortPuzzles(puzzles):
    return puzzles

'''
search algorithms='depth_first_search', 'breadth_first_search', 'best_first_search'
'''
def solve(puzzle, search_algorithm='breadth_first_search'):
    iterations = 0
    past_moves = set()
    stop_iteration = False
    tree = Tree()
    puzzles = [tree.add(puzzle, None)]
    safety = MAX_ITERATIONS

    while len(puzzles) >0 and not stop_iteration: 
        puzzle = getChild(puzzles)  # current node
        # printPuzzle(puzzle.state)
        next_moves = possibleMoves(puzzle.state, past_moves)
        past_moves.update(next_moves)

        # test if we have found the solution
        for p in next_moves:
            iterations = iterations + 1
            child = tree.add(p, puzzle)
            addChild(puzzles, child, search_algorithm)

            if child.state == '123456780':
                solution = child.getPath()
                

                ## stampa la soluzione
                for m in solution:
                    printPuzzle(m.state)   
                print(f"SOLVED!!! {len(solution)} moves !!!")
                print(f"Solution found with {iterations} iterations")
                stop_iteration = True
                return
        sortPuzzles(puzzles)
        puzzles.remove(puzzle)
        
        if safety == 0:
            stop_iteration = True

        safety = safety - 1    
    print('No solution found')
    print('iterations: ', iterations)


if __name__ == '__main__':
    puzzle = "123405678"
    #puzzle = generateRandomPuzzle()
   
    print("Current puzzle to solve")
    printPuzzle(puzzle)
     # search algorithms='depth_first_search', 'breadth_first_search', 'best_first_search'
    algo = 'depth_first_search'
    print(f"Search algorithm {algo}")
    solve(puzzle, algo)
    exit()

#generateAllPossibleMoves(puzzle)

'''
print(f'moves found: {len(moves)}')
for puzzle in moves:
    printPuzzle(puzzle)
'''


"""

This module provides a class `Puzzle8` to solve the 8-puzzle problem using different search algorithms. The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with 8 numbered tiles and one empty space. The goal is to rearrange the tiles to match a specified goal state.

Class:
    Puzzle8:
        A class to represent and solve the 8-puzzle problem.

        Attributes:
            goal (str): The goal state of the puzzle.
            allowed_algorithms (list): List of allowed search algorithms.
            puzzle (str): The current state of the puzzle.

        Methods:
            __init__(self, puzzle=None):
                Initializes the Puzzle8 instance with a given puzzle state or generates a random puzzle.

            setPuzzle(self, puzzle):
                Sets the puzzle to a given state.

            randomPuzzle(self):
                Generates a random puzzle state.

            checkAlgorithm(self, algo):
                Checks if the provided algorithm is allowed.

            printAllowedAlgorithms(self):
                Prints the list of allowed algorithms.

            generateRandomPuzzle(self):
                Generates a random puzzle state.

            printablePuzzle(self, puzzle=None):
                Returns a printable string representation of the puzzle.

            getNextPossibleMoves(self, puzzle, past_moves):
                Returns the possible moves given a puzzle state.

            addChildToPuzzleBySearchAlgorithm(self, puzzles, child, search_algorithm):
                Adds a child node to the list of puzzles to be visited based on the search algorithm.

            getPath(self, puzzle, parents):
                Returns the path from the initial state to the given puzzle state.

            pushNextNodeToVisit(self, tovisit, puzzle, algo):
                Pushes the next node to visit based on the search algorithm.

            popNextNodeToVisit(self, tovisit, algo):
                Pops the next node to visit based on the search algorithm.

            printSolution(self, solution):
                Prints the solution path.

            solve(self, algo):
                Solves the puzzle using the specified search algorithm.

            distance(self, puzzle):
                Calculates the Hamming distance between the current puzzle state and the goal state.

Usage:
    To use this library, create an instance of the `Puzzle8` class and call the `solve` method with the desired search algorithm. The allowed algorithms are "depth_first_search", "breadth_first_search", and "best_first_search". The solution path can be printed using the `printSolution` method.

    Example:
        solution = puzzle8.solve("breadth_first_search")
"""

from random import shuffle
import heapq


class Puzzle8:
    goal = "123456780"

    allowed_algorithms = [
        "depth_first_search",
        "breadth_first_search",
        "best_first_search",
        "A*",
    ]

    def __init__(self, puzzle=None):
        if puzzle is None:
            self.puzzle = self.generateRandomPuzzle()
        else:
            self.puzzle = puzzle

    def setPuzzle(self, puzzle):
        self.puzzle = puzzle

    def randomPuzzle(self):
        self.puzzle = self.generateRandomPuzzle()

    # This method checks if the provided algorithm is allowed

    def checkAlgorithm(self, algo):
        if algo not in self.allowed_algorithms:
            self.printAllowedAlgorithms()
            # throw exception
            raise ValueError(f"Algorithm {algo} not allowed")

    def printAllowedAlgorithms(self):
        print("Allowed algorithms")
        for algo in self.allowed_algorithms:
            print(algo)

    # This method generates a random puzzle

    def generateRandomPuzzle(self):
        randomArray = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        shuffle(randomArray)
        return "".join(randomArray)

    # This method prints the puzzle
    def printablePuzzle(self, puzzle=None):
        if puzzle is None:
            puzzle = self.puzzle
        str = ""
        str += "---------\n"
        for i in range(9):
            str += f" {puzzle[i]} "
            if (i - 2) % 3 == 0:
                str += "\n"
        str += "---------\n"

        return str

    # This method returns the possible moves given a puzzle state
    # no duplicate moves are returned

    def getNextPossibleMoves(self, puzzle, past_moves):
        i = puzzle.find("0")
        allowedMoves = []

        # allowing left move indexes 1,2,4,5,7,8
        if i == 1 or i == 2 or i == 4 or i == 5 or i == 7 or i == 8:
            arr = list(puzzle)
            arr[i] = arr[i - 1]
            arr[i - 1] = "0"
            if "".join(arr) not in past_moves:
                allowedMoves.append("".join(arr))

        # allowing right move indexes 0,1,3,4,6,7
        if i == 0 or i == 1 or i == 3 or i == 4 or i == 6 or i == 7:
            arr = list(puzzle)
            arr[i] = arr[i + 1]
            arr[i + 1] = "0"
            if "".join(arr) not in past_moves:
                allowedMoves.append("".join(arr))

        # allowing up move indexes 3,6,4,7,5,8
        if i == 3 or i == 6 or i == 4 or i == 7 or i == 5 or i == 8:
            arr = list(puzzle)
            arr[i] = arr[i - 3]
            arr[i - 3] = "0"
            if "".join(arr) not in past_moves:
                allowedMoves.append("".join(arr))

        # allowing down move indexes 0,1,2,3,4,5
        if i <= 5:
            arr = list(puzzle)
            arr[i] = arr[i + 3]
            arr[i + 3] = "0"
            if "".join(arr) not in past_moves:
                allowedMoves.append("".join(arr))
        return allowedMoves

    def getPath(self, puzzle, parents):
        curr = puzzle
        path = []
        while curr != None:
            path = [curr] + path
            curr = parents[curr]
        return path

    def pushNextNodeToVisit(self, tovisit, puzzle, algo, distance_type, costtoreach=0):
        if algo == "depth_first_search":
            tovisit.append(puzzle)
        elif algo == "breadth_first_search":
            tovisit.insert(0, puzzle)
        elif algo == "best_first_search":
            heapq.heappush(tovisit, [self.distance(puzzle, distance_type), puzzle])
        elif algo == "A*":
            heapq.heappush(
                tovisit, [self.distance(puzzle, distance_type) + costtoreach, puzzle]
            )
        else:
            print(f"Algorithm {algo} not implemented")
            exit()

    def popNextNodeToVisit(self, tovisit, algo):
        if algo == "depth_first_search":
            return tovisit.pop(0)
        elif algo == "breadth_first_search":
            return tovisit.pop(0)
        elif algo == "best_first_search" or algo == "A*":
            (cost, item) = heapq.heappop(tovisit)
            return item
        else:
            print(f"Algorithm {algo} not implemented")
            exit()

    def printSolution(self, solution):
        for m in solution:
            print(self.printablePuzzle(m))

    def solve(self, algo, distance_type="manhattan"):
        self.checkAlgorithm(algo)
        iterations = 0
        current = f"{self.puzzle}"
        parents = {}
        costs = {}

        parents[self.puzzle] = None  # The parent of puzzle is None
        costs[self.puzzle] = 1
        visited = set()
        tovisit = []
        self.pushNextNodeToVisit(tovisit, self.puzzle, algo, distance_type)

        while len(tovisit) > 0:
            current = self.popNextNodeToVisit(tovisit, algo)
            if current in visited:
                continue
            next_moves = self.getNextPossibleMoves(current, visited)

            # loops over possible moves
            for child in next_moves:
                iterations = iterations + 1
                parents[child] = current  # sets the parent

                hamming = self.distance(child, distance_type)
                # is the child a solution?
                if hamming == 0:
                    solution = self.getPath(child, parents)
                    print(
                        f"\t -> Solution found in {len(solution) - 1} moves with {iterations} iterations. Visited nodes: {len(visited)}"
                    )
                    return solution

                self.pushNextNodeToVisit(
                    tovisit, child, algo, distance_type, costs[current] + 1
                )
                costs[child] = costs[current] + 1
            visited.add(current)

        print("\t -> No solution found")
        return None

    def distance(self, puzzle, type):
        if type == "hamming":
            return sum(c1 != c2 for c1, c2 in zip(puzzle, self.goal))
        if type == "manhattan":
            distance = 0
            for i in range(9):
                pc = puzzle[i]
                px = i % 3
                py = i // 3
                di = self.goal.index(pc)
                dx = di % 3
                dy = di // 3
                distance += abs(px - dx) + abs(py - dy)
            return distance


if __name__ == "__main__":
    print("PUZZLE 8 SOLVER - AI Search State Space algorithms\n")
    puzzle8 = Puzzle8("123405678")
    puzzle8.solve("A*")

    # puzzle8 = Puzzle8()
    allowed_algorithms = puzzle8.allowed_algorithms
    print("Current puzzle to solve:\n")
    print(puzzle8.printablePuzzle())

    solution = None
    for algo in allowed_algorithms:
        print(f"### Search algorithm {algo} ###")
        solution = puzzle8.solve(algo, "manhattan")
        print()

    if solution:
        puzzle8.printSolution(solution)
    else:
        print("No solution found")
    exit()

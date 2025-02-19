import unittest
from puzzle8 import Puzzle8

class TestPuzzle8(unittest.TestCase):

    def setUp(self):
        self.puzzle = Puzzle8("123405678")

    def test_initial_puzzle(self):
        self.assertEqual(self.puzzle.puzzle, "123405678")

    def test_set_puzzle(self):
        self.puzzle.setPuzzle("876543210")
        self.assertEqual(self.puzzle.puzzle, "876543210")

    def test_generate_random_puzzle(self):
        random_puzzle = self.puzzle.generateRandomPuzzle()
        self.assertEqual(len(random_puzzle), 9)
        self.assertTrue(all(str(i) in random_puzzle for i in range(9)))

    def test_printable_puzzle(self):
        expected_output = "---------\n 1  2  3 \n 4  0  5 \n 6  7  8 \n---------\n"
        self.assertEqual(self.puzzle.printablePuzzle(), expected_output)

    def test_get_next_possible_moves(self):
        moves = self.puzzle.getNextPossibleMoves("123405678", set())
        expected_moves = ["123045678", "103425678", "123450678", "123475608"]
        self.assertCountEqual(moves, expected_moves)

    def test_hamming_distance(self):
        self.assertEqual(self.puzzle.distance("123405678", "hamming"), 5)
        self.assertEqual(self.puzzle.distance("123456780", "hamming"), 0)

    def test_manhattan_distance(self):
        self.assertEqual(self.puzzle.distance("123405678", "manhattan"), 8)
        self.assertEqual(self.puzzle.distance("123456780", "manhattan"), 0)
    

    def test_solve_breadth_first_search(self):
        solution = self.puzzle.solve("breadth_first_search")
        self.assertIsNotNone(solution)
        self.assertEqual(solution[-1], "123456780")

    def test_solve_depth_first_search(self):
        solution = self.puzzle.solve("depth_first_search")
        self.assertIsNotNone(solution)
        self.assertEqual(solution[-1], "123456780")

    def test_solve_best_first_search(self):
        solution = self.puzzle.solve("best_first_search")
        self.assertIsNotNone(solution)
        self.assertEqual(solution[-1], "123456780")

if __name__ == '__main__':
    unittest.main()
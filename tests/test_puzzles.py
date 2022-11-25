import unittest

from cubzone.tools.puzzles import Puzzles

puzzles = Puzzles()


class PuzzlesTestCase(unittest.TestCase):
    def test_scramble_length(self):
        puzzle_types = puzzles.get_puzzle_types()
        for puzzle_type in puzzle_types:
            scramble_program = puzzles.get_scramble_program(puzzle_type)

            scramble_length = len(scramble_program.get_scramble().split())

            self.assertEqual(scramble_length, scramble_program.scramble_length)

    def test_list_of_scrambles(self):
        scramble_program = puzzles.get_scramble_program("333")

        scrambles = scramble_program.get_scrambles(5)

        self.assertEqual(len(scrambles), 5)


if __name__ == '__main__':
    unittest.main()

from abc import ABC, abstractmethod
from enum import IntEnum
from random import choice, randint


class ScrambleLengths(IntEnum):
    two_by_two_cube_puzzle = 11
    three_by_three_cube_puzzle = 21
    four_by_four_cube_puzzle = 44
    five_by_five_cube_puzzle = 60


class Puzzle(ABC):
    scramble_length: ScrambleLengths

    def get_scramble(self) -> str:
        return self.make_scramble(self.scramble_length)

    @classmethod
    @abstractmethod
    def make_scramble(cls, scramble_length: ScrambleLengths) -> str:
        pass


class CubePuzzle(Puzzle):
    cube_faces: list
    directions: list[str] = ["", "'", "2"]

    @classmethod
    def make_scramble(cls, scramble_length: ScrambleLengths) -> str:
        scramble = ""

        cube_faces_used = []
        while scramble_length:
            random_number = randint(0, 2)
            cube_face = choice(cls.cube_faces[random_number])

            if len(cube_faces_used) and cube_faces_used[-1] == cube_face:
                continue
            if len(cube_faces_used) > 1 and (
                    cube_faces_used[-1] in cls.cube_faces[random_number] and
                    cube_faces_used[-2] in cls.cube_faces[random_number]
            ):
                continue

            cube_faces_used.append(cube_face)

            scramble += f"{cube_face}{choice(cls.directions)} "
            scramble_length -= 1

        return scramble


class TwoByTwoCubePuzzle(CubePuzzle):
    cube_faces = [("B", "F"), ("D", "U"), ("L", "R")]
    scramble_length = ScrambleLengths.two_by_two_cube_puzzle


class ThreeByThreeCubePuzzle(CubePuzzle):
    cube_faces = [("B", "F"), ("D", "U"), ("L", "R")]
    scramble_length = ScrambleLengths.three_by_three_cube_puzzle


class FourByFourCubePuzzle(CubePuzzle):
    cube_faces = [
        ("B", "Bw", "F", "Fw"),
        ("D", "Dw", "U", "Uw"),
        ("L", "Lw", "R", "Rw")
    ]
    scramble_length = (
            ScrambleLengths.four_by_four_cube_puzzle -
            ScrambleLengths.three_by_three_cube_puzzle
    )

    def get_scramble(self) -> str:
        scramble = ThreeByThreeCubePuzzle().get_scramble()

        return scramble + self.make_scramble(self.scramble_length)


class FiveByFiveCubePuzzle(CubePuzzle):
    cube_faces = [
        ("B", "Bw", "F", "Fw"),
        ("D", "Dw", "U", "Uw"),
        ("L", "Lw", "R", "Rw")
    ]
    scramble_length = ScrambleLengths.five_by_five_cube_puzzle


class Puzzles:
    scramble_programs: dict[str, Puzzle] = {
        "222": TwoByTwoCubePuzzle(),
        "333": ThreeByThreeCubePuzzle(),
        "444": FourByFourCubePuzzle(),
        "555": FiveByFiveCubePuzzle()
    }

    def get_puzzle_types(self) -> list[str]:
        return list(self.scramble_programs.keys())

    def get_scramble_program(self, puzzle_type: str) -> Puzzle:
        return self.scramble_programs.get(puzzle_type)


__all__ = ["Puzzles"]

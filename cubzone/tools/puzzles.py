from abc import ABC, abstractmethod
from enum import IntEnum
from random import choice, randint


class ScrambleLengths(IntEnum):
    TWO_BY_TWO_CUBE_PUZZLE = 11
    THREE_BY_THREE_CUBE_PUZZLE = 21
    FOUR_BY_FOUR_CUBE_PUZZLE = 44
    FIVE_BY_FIVE_CUBE_PUZZLE = 60
    SIX_BY_SIX_CUBE_PUZZLE = 80
    SEVEN_BY_SEVEN_CUBE_PUZZLE = 100


class Puzzle(ABC):
    scramble_length: ScrambleLengths

    def get_scramble(self) -> str:
        return self.make_scramble(self.scramble_length)

    def get_scrambles(self, number_of_scrambles: int) -> list[str]:
        return [self.get_scramble() for _ in range(number_of_scrambles)]

    @classmethod
    @abstractmethod
    def make_scramble(cls, scramble_length: ScrambleLengths) -> str:
        pass


class CubePuzzle(Puzzle):
    cube_faces: list[tuple[str, ...]]
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
    scramble_length = ScrambleLengths.TWO_BY_TWO_CUBE_PUZZLE


class ThreeByThreeCubePuzzle(CubePuzzle):
    cube_faces = [("B", "F"), ("D", "U"), ("L", "R")]
    scramble_length = ScrambleLengths.THREE_BY_THREE_CUBE_PUZZLE


class FourByFourCubePuzzle(CubePuzzle):
    cube_faces = [
        ("B", "F", "Fw"),
        ("D", "U", "Uw"),
        ("L", "R", "Rw")
    ]
    scramble_length = ScrambleLengths.FOUR_BY_FOUR_CUBE_PUZZLE

    def get_scramble(self) -> str:
        scramble = ThreeByThreeCubePuzzle().get_scramble()

        return scramble + self.make_scramble(
            self.scramble_length - ScrambleLengths.THREE_BY_THREE_CUBE_PUZZLE
        )


class FiveByFiveCubePuzzle(CubePuzzle):
    cube_faces = [
        ("B", "Bw", "F", "Fw"),
        ("D", "Dw", "U", "Uw"),
        ("L", "Lw", "R", "Rw")
    ]
    scramble_length = ScrambleLengths.FIVE_BY_FIVE_CUBE_PUZZLE


class SixBySixCubePuzzle(CubePuzzle):
    cube_faces = [
        ("3Fw", "B", "Bw", "F", "Fw"),
        ("3Uw", "D", "Dw", "U", "Uw"),
        ("3Rw", "L", "Lw", "R", "Rw")
    ]
    scramble_length = ScrambleLengths.SIX_BY_SIX_CUBE_PUZZLE


class SevenBySevenCubePuzzle(CubePuzzle):
    cube_faces = [
        ("3Bw", "3Fw", "B", "Bw", "F", "Fw"),
        ("3Dw", "3Uw", "D", "Dw", "U", "Uw"),
        ("3Lw", "3Rw", "L", "Lw", "R", "Rw")
    ]
    scramble_length = ScrambleLengths.SEVEN_BY_SEVEN_CUBE_PUZZLE


class Puzzles:
    scramble_programs: dict[str, Puzzle] = {
        "222": TwoByTwoCubePuzzle(),
        "333": ThreeByThreeCubePuzzle(),
        "444": FourByFourCubePuzzle(),
        "555": FiveByFiveCubePuzzle(),
        "666": SixBySixCubePuzzle(),
        "777": SevenBySevenCubePuzzle()
    }

    def get_puzzle_types(self) -> list[str]:
        return list(self.scramble_programs.keys())

    def get_scramble_program(self, puzzle_type: str) -> Puzzle:
        return self.scramble_programs.get(puzzle_type)


__all__ = ["Puzzles"]

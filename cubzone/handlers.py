from abc import ABC, abstractmethod

from database import Database
from puzzles import Puzzles

database = Database()
puzzles = Puzzles()


class CommandHandler(ABC):
    @abstractmethod
    def handle_command(self, arguments: list[str], account: int) -> str:
        pass


class HelpHandler(CommandHandler):
    def handle_command(self, arguments: list[str], account: int) -> str:
        return "vk.com/@cubzone-commands"


class PuzzlesHandler(CommandHandler):
    def handle_command(self, arguments: list[str], account: int) -> str:
        puzzle_types = ", ".join(puzzles.get_puzzle_types())

        return f"Список доступных головоломок: [ {puzzle_types} ]."


class ScrambleHandler(CommandHandler):
    def handle_command(self, arguments: list[str], account: int) -> str:
        arguments = self.handle_arguments(arguments, account)
        if isinstance(arguments, str):
            return arguments

        number_of_scrambles, puzzle_type = arguments

        scramble_program = puzzles.get_scramble_program(puzzle_type)

        if number_of_scrambles == 1:
            return scramble_program.get_scramble()
        scrambles = [
            scramble_program.get_scramble() for _ in range(number_of_scrambles)
        ]

        response = f"Количество алгоритмов: [ {len(scrambles)} ].\n\n"
        for number, scramble in enumerate(scrambles, 1):
            response += f"[ {number} ]: {scramble}\n"

        return response

    @classmethod
    def check_arguments(
            cls, number_of_scrambles: str, puzzle_type: str
    ) -> str | None:
        if not number_of_scrambles.isdigit():
            return "<Количество алгоритмов> = натуральное число от 1 до 13."
        if not 0 < int(number_of_scrambles) < 13:
            return "<Количество алгоритмов> = натуральное число от 1 до 13."

        puzzle_types = puzzles.get_puzzle_types()
        if puzzle_type not in puzzle_types:
            return (
                "<Тип головоломки> = название головоломки. "
                "Команда /puzzles для получения списка доступных головоломок."
            )

    @classmethod
    def handle_arguments(
            cls, arguments: list[str], account: int
    ) -> str | tuple:
        number_of_arguments = len(arguments)
        if number_of_arguments == 0:
            return (
                database.tables.settings.get_number_of_scrambles(account),
                database.tables.settings.get_puzzle_type(account)
            )
        elif number_of_arguments == 1:
            number_of_scrambles = arguments[0]
            puzzle_type = database.tables.settings.get_puzzle_type(account)

            error_message = cls.check_arguments(
                number_of_scrambles, puzzle_type
            )
            if error_message:
                return error_message

            return int(number_of_scrambles), puzzle_type
        elif number_of_arguments == 2:
            number_of_scrambles, puzzle_type = arguments

            error_message = cls.check_arguments(
                number_of_scrambles, puzzle_type
            )
            if error_message:
                return error_message

            return int(number_of_scrambles), puzzle_type


class SettingsHandler(CommandHandler):
    def handle_command(self, arguments: list[str], account: int) -> str:
        number_of_arguments = len(arguments)
        if number_of_arguments == 2:
            number_of_scrambles, puzzle_type = arguments

            error_message = ScrambleHandler.check_arguments(
                number_of_scrambles, puzzle_type
            )
            if error_message:
                return error_message

            database.tables.settings.update_settings(
                number_of_scrambles, puzzle_type, account
            )

            return (
                f"Новые значения по умолчанию [ {number_of_scrambles}, "
                f"{puzzle_type} ] для команды /scramble успешно установлены."
            )
        else:
            settings = (
                database.tables.settings.get_number_of_scrambles(account),
                database.tables.settings.get_puzzle_type(account)
            )

            number_of_scrambles, puzzle_type = settings

            return (
                f"Количество алгоритмов: [ {number_of_scrambles} ].\n"
                f"Тип головоломки: [ {puzzle_type} ]."
            )


class Handlers:
    command_handlers = {
        "help": HelpHandler(),
        "puzzles": PuzzlesHandler(),
        "scramble": ScrambleHandler(),
        "settings": SettingsHandler()
    }

    def get_command_handler(self, command_name: str) -> CommandHandler:
        command_name = command_name.replace("/", "")

        return self.command_handlers.get(command_name)


__all__ = ["Handlers"]

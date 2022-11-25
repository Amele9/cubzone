import unittest

from cubzone.tools.handlers import Handlers

handlers = Handlers()


class HandlersTestCase(unittest.TestCase):
    def test_scramble_handler(self):
        command_handler = handlers.get_command_handler("/scramble")

        self.assertEqual(
            command_handler.handle_command(["0"], 1),
            "<Количество алгоритмов> = натуральное число от 1 до 13."
        )
        self.assertEqual(
            command_handler.handle_command(["5", "000"], 1),
            (
                "<Тип головоломки> = название головоломки. "
                "Команда /puzzles для получения списка доступных головоломок."
            )
        )

    def test_settings_handler(self):
        command_handler = handlers.get_command_handler("/settings")

        self.assertEqual(
            command_handler.handle_command([], 1),
            (
                "Количество алгоритмов: [ 1 ].\n"
                "Тип головоломки: [ 333 ]."
            )
        )


if __name__ == '__main__':
    unittest.main()

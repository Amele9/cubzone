# CubZone

CubZone - это сообщество (бот), которое генерирует алгоритмы для разборки
головоломок типа кубика Рубика. [Ссылка на сообщество](https://vk.com/cubzone).

## Список команд

### Введение

Команды начинаются со знака `/`.

Аргументы в угловых скобках `<>` __обязательны__.
Аргументы в круглых скобках `()` __необязательны__.

### Команды

#### puzzles

> Отправляет в чат список доступных головоломок для команды scramble.

> [Список доступных головоломок](#список-доступных-головоломок).

#### scramble (`number_of_scrambles`) (`puzzle_type`)

> Отправляет в чат алгоритм для разборки головоломки.

> Описание аргументов команды scramble:

| Название аргумента  | Его описание                  |
|---------------------|-------------------------------|
| number_of_scrambles | натуральное число от 1 до 13. |
| puzzle_type         | название головоломки.         |

> Аргументы по умолчанию:
> - количество алгоритмов = 1
> - тип головоломки = 333.

#### settings (`number_of_scrambles`) (`puzzle_type`)

> Обновляет или отправляет в чат ваши аргументы по умолчанию для команды
> scramble.

> Описание аргументов команды settings:

| Название аргумента  | Его описание                  |
|---------------------|-------------------------------|
| number_of_scrambles | натуральное число от 1 до 13. |
| puzzle_type         | название головоломки.         |

### Список доступных головоломок

- 222
- 333
- 444
- 555
- 666
- 777
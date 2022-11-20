import logging
from os import getenv

from vkbottle.bot import Bot, Message

from cubzone.handlers import Handlers

logging.getLogger("vkbottle").setLevel(logging.INFO)

bot = Bot(token=getenv("token"))

handlers = Handlers()


@bot.labeler.message()
async def message_handler(message: Message):
    command_data = message.text.split()
    if not command_data:
        return None

    command_name = command_data[0]
    command_handler = handlers.get_command_handler(command_name)
    if not command_handler:
        return None

    command_arguments = command_data[1:]
    response = command_handler.handle_command(
        command_arguments, message.from_id
    )

    await message.reply(response)


bot.run_forever()

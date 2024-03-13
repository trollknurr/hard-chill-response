import logging

from dependency_injector.wiring import Provide, inject
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

from adapter.input.tg_echo_message import TelegramEchoText
from domain.models import HumanTextInput
from tg_bot.container import Container

# TODO: Cool logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


@inject
async def echo(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    echo_text_input: TelegramEchoText = Provide[Container.echo_text_input],
) -> None:
    if update.message is None:
        return

    if update.message.text is None:
        return

    message = HumanTextInput(message=update.message.text)
    response = echo_text_input.get_text(message)
    await update.message.reply_text(response.message)


@inject
def main(tg_app: Application = Provide[Container.tg_app]) -> None:
    logger.info("Boy, i'm starting up!")
    tg_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    tg_app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    container = Container()
    container.init_resources()

    container.wire(modules=[__name__])
    main()

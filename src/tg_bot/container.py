from dependency_injector import containers, providers

from adapter.input.tg_echo_message import TelegramEchoText
from application.service.echo_message_service import EchoTextService
from tg_bot.config import Config
from tg_bot.telegram import tg_app_factory


class Container(containers.DeclarativeContainer):
    config: Config = Config()

    tg_app = providers.Singleton(tg_app_factory, bot_token=config.BOT_TOKEN)

    echo_text_service = providers.Factory(EchoTextService)
    echo_text_input = providers.Factory(TelegramEchoText, echo=echo_text_service)

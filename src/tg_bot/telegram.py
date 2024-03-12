from pydantic import SecretStr
from telegram.ext import Application, ApplicationBuilder


def tg_app_factory(bot_token: SecretStr) -> Application:
    return ApplicationBuilder().token(bot_token.get_secret_value()).build()

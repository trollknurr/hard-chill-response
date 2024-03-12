from application.port.input.echo_message import EchoText
from domain.models import BotTextOutput, HumanTextInput


class TelegramEchoText:
    def __init__(self, echo: EchoText) -> None:
        self._echo = echo

    def get_text(self, message: HumanTextInput) -> BotTextOutput:
        return self._echo.echo(message)

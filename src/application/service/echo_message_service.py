import logging

from application.port.input.echo_message import EchoText
from domain.models import BotTextOutput, HumanTextInput


class EchoTextService(EchoText):
    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

    def echo(self, message: HumanTextInput) -> BotTextOutput:
        self._logger.info(f"Echoing message: {message.message}")
        return BotTextOutput(message=message.message)

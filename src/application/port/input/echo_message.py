import abc

from domain.models import BotTextOutput, HumanTextInput


class EchoText(abc.ABC):
    @abc.abstractmethod
    def echo(self, message: HumanTextInput) -> BotTextOutput:
        pass

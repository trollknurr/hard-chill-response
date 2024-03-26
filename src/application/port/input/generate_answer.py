import abc

from domain.models import BotAnswer, UserQuestion


class GenerateAnswer(abc.ABC):
    @abc.abstractmethod
    def answer(self, user_input: UserQuestion) -> BotAnswer:
        raise NotImplementedError

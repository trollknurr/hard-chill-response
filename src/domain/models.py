from pydantic.dataclasses import dataclass


@dataclass
class HumanTextInput:
    message: str


@dataclass
class BotTextOutput:
    message: str

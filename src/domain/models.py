from enum import StrEnum

from pydantic.dataclasses import dataclass


@dataclass
class HumanTextInput:
    message: str


@dataclass
class BotTextOutput:
    message: str


@dataclass
class UserQuestion:
    question: str
    user_id: str


class SourceType(StrEnum):
    RAW_TEXT = "raw_text"
    DOCUMENT = "document"
    AUDIO = "audio"


@dataclass
class AnswerSource:
    source_id: str
    source_type: SourceType
    source_name: str
    content: str


@dataclass
class BotAnswer:
    answer: str
    sources: list[AnswerSource]

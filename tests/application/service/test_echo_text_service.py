import pytest
from src.application.service.echo_message_service import EchoTextService
from src.application.service.echo_message_service import HumanTextInput, BotTextOutput


@pytest.fixture()
def echo_service():
    return EchoTextService()


@pytest.fixture()
def test_message_text():
    return "Hello, World!"


@pytest.fixture()
def input_message(test_message_text: str):
    return HumanTextInput(message=test_message_text)


@pytest.fixture()
def expected_output(test_message_text: str):
    return BotTextOutput(message=test_message_text)


def test_echo(echo_service, input_message, expected_output):
    assert echo_service.echo(input_message) == expected_output

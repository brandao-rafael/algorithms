from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = "subinoonibus"

    odd = encrypt_message(message, 5)
    even = encrypt_message(message, 6)
    inverted = encrypt_message(message, 30)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message, "b")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1008, 3)
    assert odd == "nibus_subinoo"
    assert even == "subino_onibus"
    assert inverted == message

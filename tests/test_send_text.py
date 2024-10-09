from lib.send_text import SendText
from unittest.mock import Mock

text1 = SendText(1234)
def test_creates_instance():
    assert isinstance(text1, SendText)
    assert text1.number == 1234

def test_format_text_makes_get_request():
    new_text = SendText('+447543546071')
    assert new_text.number == '+447543546071'
    assert new_text.format_text() == "Thank you for your order. Your delivery is scheduled for today at 18:00. If you need to change it, please reply back and let us know."
# tests/test_main.py

from yamini_hello.main import hello

def test_hello(capsys):
    hello("Yamini")
    captured = capsys.readouterr()
    assert "Hello, Yamini!" in captured.out

# DON'T TOUCH THIS FILE
from main import main


def test1(monkeypatch, capsys):
    inputs = iter(['geheim', 'B', 'E', '12.50', 'Z', 'A', '5', '7', '2', '31', '39', '13', '4', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    assert True

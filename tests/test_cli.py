import sys

from toolkit.__main__ import main


def test_cli_valid_calculation(capsys):
    sys.argv = ["toolkit", "calc", "77/7"]
    try:
        main()
    except SystemExit as e:
        assert e.code == 0

    captured = capsys.readouterr()
    assert float(captured.out) == 11.0


def test_cli_valid_conversion(capsys):
    sys.argv = ["toolkit", "convert", "77", "--from", "m", "--to", "cm"]

    try:
        main()
    except SystemExit as e:
        assert e.code == 0

    captured = capsys.readouterr()
    assert float(captured.out) == 7700.0

def test_cli_valid_help():
    sys.argv = ["toolkit", "--help"]

    try:
        main()
    except SystemExit as e:
        assert e.code == 0
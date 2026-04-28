from pathlib import Path

from hackasm.parser import Parser


def test_has_more_commands_returns_true_until_end_of_file(tmp_path: Path) -> None:
    asm_file = tmp_path / "Add.asm"
    asm_file.write_text(
        "@2\n" "D=A\n" "@3\n" "D=D+A\n",
        encoding="utf-8",
    )

    parser = Parser(asm_file)

    assert parser.hasMoreCommands() is True


def test_has_more_commands_returns_false_for_empty_file(tmp_path: Path) -> None:
    asm_file = tmp_path / "Empty.asm"
    asm_file.write_text("", encoding="utf-8")

    parser = Parser(asm_file)

    assert parser.hasMoreCommands() is False


def test_has_more_commands_ignores_blank_lines_and_comments(tmp_path: Path) -> None:
    asm_file = tmp_path / "CommentsOnly.asm"
    asm_file.write_text(
        "// comment\n" "\n" "   \n" "// another comment\n",
        encoding="utf-8",
    )

    parser = Parser(asm_file)

    assert parser.hasMoreCommands() is False


def test_has_more_commands_returns_false_for_empty_file(tmp_path: Path) -> None:
    asm_file = tmp_path / "Empty.asm"
    asm_file.write_text("", encoding="utf-8")

    parser = Parser(asm_file)

    assert parser.hasMoreCommands() is False


def test_has_more_commands_returns_false_for_comments_and_blank_lines_only(tmp_path):
    asm_file = tmp_path / "CommentsOnly.asm"
    asm_file.write_text(
        "\n" "// comment\n" "   \n" "// another comment\n",
        encoding="utf-8",
    )

    parser = Parser(asm_file)

    assert parser.hasMoreCommands() is False


def test_has_more_commands_allows_indented_commands(tmp_path):
    asm_file = tmp_path / "Indented.asm"
    asm_file.write_text("   @2\n", encoding="utf-8")

    parser = Parser(asm_file)

    assert parser.hasMoreCommands() is True

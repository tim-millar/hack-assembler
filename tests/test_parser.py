from pathlib import Path

from hackasm.parser import Parser


def write_asm(tmp_path: Path, contents: str) -> Path:
    asm_file = tmp_path / "Prog.asm"
    asm_file.write_text(contents, encoding="utf-8")
    return asm_file


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


def test_advance_moves_to_first_command(tmp_path: Path) -> None:
    asm_file = tmp_path / "Add.asm"
    asm_file.write_text(
        "@2\n" "D=A\n",
        encoding="utf-8",
    )

    parser = Parser(asm_file)
    assert parser.cursor is None

    parser.advance()
    assert parser.cursor == 0


def test_advance_moves_to_next_command(tmp_path: Path) -> None:
    asm_file = tmp_path / "Add.asm"
    asm_file.write_text(
        "@2\n" "D=A\n" "@3\n",
        encoding="utf-8",
    )

    parser = Parser(asm_file)

    parser.advance()
    assert parser.cursor == 0

    parser.advance()
    assert parser.cursor == 1


def test_advance_skips_blank_lines_and_comments(tmp_path: Path) -> None:
    asm_file = tmp_path / "WhitespaceAndComments.asm"
    asm_file.write_text(
        "\n" "// comment\n" "@2\n" "\n" "D=A\n",
        encoding="utf-8",
    )

    parser = Parser(asm_file)

    parser.advance()
    assert parser.cursor == 0

    parser.advance()
    assert parser.cursor == 1


def test_advance_on_empty_file_does_not_create_available_command(
    tmp_path: Path,
) -> None:
    asm_file = write_asm(tmp_path, "")

    parser = Parser(asm_file)
    assert parser.hasMoreCommands() is False

    parser.advance()
    assert parser.hasMoreCommands() is False


def test_advance_on_comments_only_file_does_not_create_available_command(
    tmp_path: Path,
) -> None:
    asm_file = write_asm(
        tmp_path,
        "\n" "// comment\n" "   \n" "// another comment\n",
    )

    parser = Parser(asm_file)
    assert parser.hasMoreCommands() is False

    parser.advance()
    assert parser.hasMoreCommands() is False


def test_has_more_commands_becomes_false_after_advancing_to_only_command(
    tmp_path: Path,
) -> None:
    asm_file = write_asm(tmp_path, "@2\n")

    parser = Parser(asm_file)
    assert parser.hasMoreCommands() is True

    parser.advance()
    assert parser.hasMoreCommands() is False


def test_has_more_commands_tracks_multiple_advances(tmp_path: Path) -> None:
    asm_file = write_asm(
        tmp_path,
        "@2\n" "D=A\n" "@3\n",
    )

    parser = Parser(asm_file)
    assert parser.hasMoreCommands() is True

    parser.advance()
    assert parser.hasMoreCommands() is True

    parser.advance()
    assert parser.hasMoreCommands() is True

    parser.advance()
    assert parser.hasMoreCommands() is False


def test_advance_counts_commands_not_raw_lines(tmp_path: Path) -> None:
    asm_file = write_asm(
        tmp_path,
        "\n" "// comment\n" "@2\n" "\n" "// another comment\n" "D=A\n",
    )

    parser = Parser(asm_file)
    assert parser.hasMoreCommands() is True

    parser.advance()
    assert parser.hasMoreCommands() is True

    parser.advance()
    assert parser.hasMoreCommands() is False


def test_command_type_for_a_command(tmp_path: Path) -> None:
    asm_file = write_asm(tmp_path, "@2\n")

    parser = Parser(asm_file)
    parser.advance()

    assert parser.commandType() == "A_COMMAND"


def test_command_type_for_c_command(tmp_path: Path) -> None:
    asm_file = write_asm(tmp_path, "D=A\n")

    parser = Parser(asm_file)
    parser.advance()

    assert parser.commandType() == "C_COMMAND"


def test_command_type_for_l_command(tmp_path: Path) -> None:
    asm_file = write_asm(tmp_path, "(LOOP)\n")

    parser = Parser(asm_file)
    parser.advance()

    assert parser.commandType() == "L_COMMAND"


def test_command_type_tracks_current_command_after_multiple_advances(
    tmp_path: Path,
) -> None:
    asm_file = write_asm(
        tmp_path,
        "@2\n" "D=A\n" "(LOOP)\n",
    )

    parser = Parser(asm_file)

    parser.advance()
    assert parser.commandType() == "A_COMMAND"

    parser.advance()
    assert parser.commandType() == "C_COMMAND"

    parser.advance()
    assert parser.commandType() == "L_COMMAND"


def test_command_type_ignores_blank_lines_and_comments(tmp_path: Path) -> None:
    asm_file = write_asm(
        tmp_path,
        "\n" "// comment\n" "@2\n" "\n" "D=A\n",
    )

    parser = Parser(asm_file)

    parser.advance()
    assert parser.commandType() == "A_COMMAND"

    parser.advance()
    assert parser.commandType() == "C_COMMAND"

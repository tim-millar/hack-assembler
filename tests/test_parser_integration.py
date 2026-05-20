from pathlib import Path

from hackasm.parser import Parser


def write_asm(tmp_path: Path, contents: str) -> Path:
    asm_file = tmp_path / "Prog.asm"
    asm_file.write_text(contents, encoding="utf-8")
    return asm_file


def test_parser_walks_mixed_commands_in_order(tmp_path: Path) -> None:
    asm_file = write_asm(
        tmp_path,
        "@2\n" "D=A\n" "(LOOP)\n" "0;JMP\n",
    )

    parser = Parser(asm_file)

    parser.advance()
    assert parser.commandType() == "A_COMMAND"
    assert parser.symbol() == "2"

    parser.advance()
    assert parser.commandType() == "C_COMMAND"
    assert parser.dest() == "D"
    assert parser.comp() == "A"
    assert parser.jump() is None

    parser.advance()
    assert parser.commandType() == "L_COMMAND"
    assert parser.symbol() == "LOOP"

    parser.advance()
    assert parser.commandType() == "C_COMMAND"
    assert parser.dest() is None
    assert parser.comp() == "0"
    assert parser.jump() == "JMP"


def test_parser_walks_commands_while_has_more_commands_is_true(tmp_path: Path) -> None:
    asm_file = write_asm(
        tmp_path,
        "@2\n" "D=A\n" "@3\n" "D=D+A\n",
    )

    parser = Parser(asm_file)

    seen_command_types = []

    while parser.hasMoreCommands():
        parser.advance()
        seen_command_types.append(parser.commandType())

    assert seen_command_types == [
        "A_COMMAND",
        "C_COMMAND",
        "A_COMMAND",
        "C_COMMAND",
    ]


def test_parser_ignores_non_command_lines_during_full_walk(tmp_path: Path) -> None:
    asm_file = write_asm(
        tmp_path,
        "\n" "// first comment\n" "@2\n" "\n" "D=A\n" "// final comment\n",
    )

    parser = Parser(asm_file)

    seen_command_types = []

    while parser.hasMoreCommands():
        parser.advance()
        seen_command_types.append(parser.commandType())

    assert seen_command_types == [
        "A_COMMAND",
        "C_COMMAND",
    ]

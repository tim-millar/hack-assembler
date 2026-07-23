from pathlib import Path

from hackasm.assembler import assemble_file


def assemble(tmp_path: Path, source: str) -> str:
    asm_file = tmp_path / "Prog.asm"
    hack_file = tmp_path / "Prog.hack"

    asm_file.write_text(source, encoding="utf-8")
    assemble_file(asm_file, hack_file)

    return hack_file.read_text(encoding="utf-8")


def test_assembles_single_a_instruction(tmp_path: Path) -> None:
    assert assemble(tmp_path, "@2\n") == "0000000000000010\n"


def test_assembles_simple_a_and_c_instructions(tmp_path: Path) -> None:
    assert assemble(
        tmp_path,
        "@2\n" "D=A\n",
    ) == ("0000000000000010\n" "1110110000010000\n")


def test_assembles_a_instruction_with_zero(tmp_path: Path) -> None:
    assert assemble(tmp_path, "@0\n") == "0000000000000000\n"


def test_assembles_largest_valid_a_instruction(tmp_path: Path) -> None:
    assert assemble(tmp_path, "@32767\n") == "0111111111111111\n"


def test_assembles_c_instruction_with_dest_only(tmp_path: Path) -> None:
    assert assemble(tmp_path, "D=M\n") == "1111110000010000\n"


def test_assembles_c_instruction_with_jump_only(tmp_path: Path) -> None:
    assert assemble(tmp_path, "0;JMP\n") == "1110101010000111\n"


def test_assembles_c_instruction_with_jump(tmp_path: Path) -> None:
    assert assemble(tmp_path, "D+1;JGT\n") == "1110011111000001\n"


def test_assembles_multiple_c_instruction_forms(tmp_path: Path) -> None:
    assert assemble(
        tmp_path,
        "D=A\n" "M=D\n" "D;JGT\n" "0;JMP\n",
    ) == (
        "1110110000010000\n"
        "1110001100001000\n"
        "1110001100000001\n"
        "1110101010000111\n"
    )


def test_ignores_blank_lines(tmp_path: Path) -> None:
    assert assemble(
        tmp_path,
        "\n" "@2\n" "\n" "D=A\n" "\n",
    ) == ("0000000000000010\n" "1110110000010000\n")


def test_ignores_full_line_comments(tmp_path: Path) -> None:
    assert assemble(
        tmp_path,
        "// Load two\n" "@2\n" "// Store it in D\n" "D=A\n",
    ) == ("0000000000000010\n" "1110110000010000\n")


def test_ignores_inline_comments(tmp_path: Path) -> None:
    assert assemble(
        tmp_path,
        "@2 // Load two\n" "D=A // Store it in D\n",
    ) == ("0000000000000010\n" "1110110000010000\n")


def test_ignores_surrounding_whitespace(tmp_path: Path) -> None:
    assert assemble(
        tmp_path,
        "   @2   \n" "\tD=A\t\n",
    ) == ("0000000000000010\n" "1110110000010000\n")


# def test_assembles_predefined_register_symbol(tmp_path: Path) -> None:
#     assert assemble(tmp_path, "@R0\n") == "0000000000000000\n"


# def test_assembles_highest_predefined_register_symbol(tmp_path: Path) -> None:
#     assert assemble(tmp_path, "@R15\n") == "0000000000001111\n"


# def test_assembles_predefined_memory_symbols(tmp_path: Path) -> None:
#     assert assemble(
#         tmp_path,
#         "@SP\n" "@LCL\n" "@ARG\n" "@THIS\n" "@THAT\n" "@SCREEN\n" "@KBD\n",
#     ) == (
#         "0000000000000000\n"
#         "0000000000000001\n"
#         "0000000000000010\n"
#         "0000000000000011\n"
#         "0000000000000100\n"
#         "0100000000000000\n"
#         "0110000000000000\n"
#     )


# def test_resolves_label_to_rom_address(tmp_path: Path) -> None:
#     assert assemble(
#         tmp_path,
#         "@START\n" "0;JMP\n" "(START)\n" "@START\n" "0;JMP\n",
#     ) == (
#         "0000000000000010\n"
#         "1110101010000111\n"
#         "0000000000000010\n"
#         "1110101010000111\n"
#     )


# def test_label_does_not_generate_machine_instruction(tmp_path: Path) -> None:
#     assert assemble(
#         tmp_path,
#         "(LOOP)\n" "@0\n" "0;JMP\n",
#     ) == ("0000000000000000\n" "1110101010000111\n")

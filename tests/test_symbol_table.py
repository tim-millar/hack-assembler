from hackasm.symbol_table import SymbolTable


def test_contains_sp() -> None:
    table = SymbolTable()

    assert table.contains("SP") is True


def test_contains_lcl() -> None:
    table = SymbolTable()

    assert table.contains("LCL") is True


def test_contains_arg() -> None:
    table = SymbolTable()

    assert table.contains("ARG") is True


def test_contains_this() -> None:
    table = SymbolTable()

    assert table.contains("THIS") is True


def test_contains_that() -> None:
    table = SymbolTable()

    assert table.contains("THAT") is True


def test_contains_screen() -> None:
    table = SymbolTable()

    assert table.contains("SCREEN") is True


def test_contains_kbd() -> None:
    table = SymbolTable()

    assert table.contains("KBD") is True


def test_contains_r_registers() -> None:
    table = SymbolTable()

    for i in range(16):
        assert table.contains(f"R{i}") is True


def test_does_not_contain_unknown_symbol() -> None:
    table = SymbolTable()

    assert table.contains("LOOP") is False


def test_does_not_contain_lowercase_predefined_symbol() -> None:
    table = SymbolTable()

    assert table.contains("sp") is False


def test_get_address_for_sp() -> None:
    table = SymbolTable()

    assert table.getAddress("SP") == 0


def test_get_address_for_lcl() -> None:
    table = SymbolTable()

    assert table.getAddress("LCL") == 1


def test_get_address_for_arg() -> None:
    table = SymbolTable()

    assert table.getAddress("ARG") == 2


def test_get_address_for_this() -> None:
    table = SymbolTable()

    assert table.getAddress("THIS") == 3


def test_get_address_for_that() -> None:
    table = SymbolTable()

    assert table.getAddress("THAT") == 4


def test_get_address_for_screen() -> None:
    table = SymbolTable()

    assert table.getAddress("SCREEN") == 16384


def test_get_address_for_kbd() -> None:
    table = SymbolTable()

    assert table.getAddress("KBD") == 24576


def test_get_address_for_r_registers() -> None:
    table = SymbolTable()

    for i in range(16):
        assert table.getAddress(f"R{i}") == i


def test_add_entry_makes_symbol_available() -> None:
    table = SymbolTable()

    table.addEntry("LOOP", 10)

    assert table.contains("LOOP") is True


def test_add_entry_stores_symbol_address() -> None:
    table = SymbolTable()

    table.addEntry("LOOP", 10)

    assert table.getAddress("LOOP") == 10


def test_add_entry_stores_multiple_symbols() -> None:
    table = SymbolTable()

    table.addEntry("LOOP", 10)
    table.addEntry("END", 22)
    table.addEntry("counter", 16)

    assert table.getAddress("LOOP") == 10
    assert table.getAddress("END") == 22
    assert table.getAddress("counter") == 16


def test_add_entry_keeps_symbol_names_distinct_by_case() -> None:
    table = SymbolTable()

    table.addEntry("LOOP", 10)
    table.addEntry("loop", 11)

    assert table.getAddress("LOOP") == 10
    assert table.getAddress("loop") == 11


def test_add_entry_allows_address_zero() -> None:
    table = SymbolTable()

    table.addEntry("START", 0)

    assert table.getAddress("START") == 0


def test_add_entry_allows_large_address() -> None:
    table = SymbolTable()

    table.addEntry("SCREEN_ALIAS", 16384)

    assert table.getAddress("SCREEN_ALIAS") == 16384

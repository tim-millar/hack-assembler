from hackasm.code import Code


def test_dest_for_null_destination() -> None:
    assert Code.dest(None) == "000"


def test_dest_for_m_destination() -> None:
    assert Code.dest("M") == "001"


def test_dest_for_d_destination() -> None:
    assert Code.dest("D") == "010"


def test_dest_for_md_destination() -> None:
    assert Code.dest("MD") == "011"


def test_dest_for_a_destination() -> None:
    assert Code.dest("A") == "100"


def test_dest_for_am_destination() -> None:
    assert Code.dest("AM") == "101"


def test_dest_for_ad_destination() -> None:
    assert Code.dest("AD") == "110"


def test_dest_for_amd_destination() -> None:
    assert Code.dest("AMD") == "111"


def test_comp_for_zero() -> None:
    assert Code.comp("0") == "0101010"


def test_comp_for_one() -> None:
    assert Code.comp("1") == "0111111"


def test_comp_for_minus_one() -> None:
    assert Code.comp("-1") == "0111010"


def test_comp_for_d() -> None:
    assert Code.comp("D") == "0001100"


def test_comp_for_a() -> None:
    assert Code.comp("A") == "0110000"


def test_comp_for_m() -> None:
    assert Code.comp("M") == "1110000"


def test_comp_for_not_d() -> None:
    assert Code.comp("!D") == "0001101"


def test_comp_for_not_a() -> None:
    assert Code.comp("!A") == "0110001"


def test_comp_for_not_m() -> None:
    assert Code.comp("!M") == "1110001"


def test_comp_for_minus_d() -> None:
    assert Code.comp("-D") == "0001111"


def test_comp_for_minus_a() -> None:
    assert Code.comp("-A") == "0110011"


def test_comp_for_minus_m() -> None:
    assert Code.comp("-M") == "1110011"


def test_comp_for_d_plus_one() -> None:
    assert Code.comp("D+1") == "0011111"


def test_comp_for_a_plus_one() -> None:
    assert Code.comp("A+1") == "0110111"


def test_comp_for_m_plus_one() -> None:
    assert Code.comp("M+1") == "1110111"


def test_comp_for_d_minus_one() -> None:
    assert Code.comp("D-1") == "0001110"


def test_comp_for_a_minus_one() -> None:
    assert Code.comp("A-1") == "0110010"


def test_comp_for_m_minus_one() -> None:
    assert Code.comp("M-1") == "1110010"


def test_comp_for_d_plus_a() -> None:
    assert Code.comp("D+A") == "0000010"


def test_comp_for_d_plus_m() -> None:
    assert Code.comp("D+M") == "1000010"


def test_comp_for_d_minus_a() -> None:
    assert Code.comp("D-A") == "0010011"


def test_comp_for_d_minus_m() -> None:
    assert Code.comp("D-M") == "1010011"


def test_comp_for_a_minus_d() -> None:
    assert Code.comp("A-D") == "0000111"


def test_comp_for_m_minus_d() -> None:
    assert Code.comp("M-D") == "1000111"


def test_comp_for_d_and_a() -> None:
    assert Code.comp("D&A") == "0000000"


def test_comp_for_d_and_m() -> None:
    assert Code.comp("D&M") == "1000000"


def test_comp_for_d_or_a() -> None:
    assert Code.comp("D|A") == "0010101"


def test_comp_for_d_or_m() -> None:
    assert Code.comp("D|M") == "1010101"

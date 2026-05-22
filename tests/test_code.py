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

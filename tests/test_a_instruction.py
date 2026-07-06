from hackasm.a_instruction import AInstruction


def test_encode_zero() -> None:
    assert AInstruction.encode("0") == "0000000000000000"


def test_encode_one() -> None:
    assert AInstruction.encode("1") == "0000000000000001"


def test_encode_two() -> None:
    assert AInstruction.encode("2") == "0000000000000010"


def test_encode_three() -> None:
    assert AInstruction.encode("3") == "0000000000000011"


def test_encode_fifteen() -> None:
    assert AInstruction.encode("15") == "0000000000001111"


def test_encode_sixteen() -> None:
    assert AInstruction.encode("16") == "0000000000010000"


def test_encode_maximum_15_bit_value() -> None:
    assert AInstruction.encode("32767") == "0111111111111111"

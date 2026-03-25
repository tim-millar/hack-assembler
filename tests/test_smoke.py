from pathlib import Path
import pytest

from hackasm.cli import assemble


def test_assemble_not_implemented_yet(tmp_path: Path) -> None:
    p = tmp_path / "Prog.asm"
    p.write_text("@2\nD=A\n", encoding="utf-8")
    with pytest.raises(NotImplementedError):
        assemble(p)

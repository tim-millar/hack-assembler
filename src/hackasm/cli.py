from __future__ import annotations

import argparse
from pathlib import Path
import sys


def assemble(asm_path: Path) -> list[str]:
    """
    Placeholder: return list of 16-bit binary strings (e.g. '0000000000000000').
    Implement the two-pass assembler logic from nand2tetris here.
    """
    # TODO: replace with real implementation
    raise NotImplementedError("Assembler not implemented yet")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="hackasm",
        description="Hack Assembler (nand2tetris Chapter 6)",
    )
    parser.add_argument("input", type=Path, help="Path to .asm input file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output .hack file path (default: same name as input with .hack)",
    )

    args = parser.parse_args(argv)

    in_path: Path = args.input
    if not in_path.exists():
        print(f"error: input file not found: {in_path}", file=sys.stderr)
        return 2
    if in_path.suffix.lower() != ".asm":
        print("warning: input does not end with .asm (continuing)", file=sys.stderr)

    out_path: Path = args.output or in_path.with_suffix(".hack")

    try:
        binary_lines = assemble(in_path)
    except NotImplementedError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    out_path.write_text("\n".join(binary_lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "main":
    raise SystemExit(main())

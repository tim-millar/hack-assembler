from functools import cached_property


class Parser:
    def __init__(self, file):
        self.file = open(file, "rb")
        self.cursor = None
        self.currentCommand = None
        self.endOfFile = False

    @cached_property
    def _file_contents(self):
        with self.file as f:
            lines = f.read().decode("utf-8").splitlines()
            print(lines)
            return lines

    def _ignore_line(s):
        return s == "" or s.startswith("//") or s.startswith("\n") or s[:1].isspace()

    def _programme(self):
        return [
            line.strip()
            for line in self._file_contents
            if not Parser._ignore_line(line.strip())
        ]

    def hasMoreCommands(self):
        if self.cursor is None:
            return len(self._programme()) > 0
        else:
            return self.cursor < len(self._programme()) - 1

    def advance(self):
        if self.cursor is None:
            self.cursor = 0
        else:
            self.cursor += 1

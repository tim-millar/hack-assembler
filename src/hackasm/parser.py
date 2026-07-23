from functools import cached_property

A_COMMAND = "A_COMMAND"
C_COMMAND = "C_COMMAND"
L_COMMAND = "L_COMMAND"


class Parser:
    def __init__(self, file):
        self.file = open(file, "rb")
        self.cursor = None
        self.currentCommand = None
        self.endOfFile = False

    def hasMoreCommands(self) -> bool:
        if self.cursor is None:
            return len(self._programme()) > 0
        else:
            return self.cursor < len(self._programme()) - 1

    def advance(self) -> int:
        if self.cursor is None:
            self.cursor = 0
        else:
            self.cursor += 1

    def commandType(self) -> str:
        current = self._programme()[self.cursor]
        current_command = current.split("//")[0].strip()

        if current_command.startswith("@"):
            return A_COMMAND
        if current_command.startswith("(") and current_command.endswith(")"):
            return L_COMMAND
        if all(c.isalpha() or c in "-+!01&;=" for c in current_command):
            return C_COMMAND

    def symbol(self) -> str | None:
        current = self._programme()[self.cursor]
        current_command = current.split("//")[0].strip()

        if self.commandType() == A_COMMAND:
            return current_command[1:]
        if self.commandType() == L_COMMAND:
            return current_command[1:-1]

    def dest(self) -> str | None:
        current = self._programme()[self.cursor]
        current_command = current.split("//")[0].strip()

        if "=" not in current_command:
            return None

        return current_command.split("=")[0]

    def comp(self) -> str:
        current = self._programme()[self.cursor]
        current_command = current.split("//")[0].strip()

        dest_comp = current_command.split(";")[0]

        if "=" in dest_comp:
            return dest_comp.split("=")[1]

        return dest_comp

    def jump(self) -> str | None:
        current = self._programme()[self.cursor]
        current_command = current.split("//")[0].strip()

        if ";" not in current_command:
            return None

        return current_command.split(";")[1]

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
            line.strip().replace(" ", "")
            for line in self._file_contents
            if not Parser._ignore_line(line.strip())
        ]

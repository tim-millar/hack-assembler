class Code:
    @staticmethod
    def dest(assembly) -> str:
        if assembly is None:
            return "000"

        machine_code = {
            "M": "001",
            "D": "010",
            "A": "100",
            "MD": "011",
            "AM": "101",
            "AD": "110",
            "AMD": "111",
        }

        return machine_code[assembly]

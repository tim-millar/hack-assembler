from hackasm.parser import Parser
from hackasm.code import Code
from hackasm.a_instruction import AInstruction


def assemble_file(asm_file, hack_file):
    parser = Parser(asm_file)

    with open(hack_file, "w", encoding="utf-8") as f:
        while parser.hasMoreCommands():
            parser.advance()

            if parser.commandType() == "A_COMMAND":
                print("A command")
                assembly = parser.symbol()
                code = AInstruction.encode(assembly)

            if parser.commandType() == "C_COMMAND":
                print("C command")
                codeDest = parser.dest()
                codeComp = parser.comp()
                codeJump = parser.jump()

                prefix = "111"
                comp = Code.comp(codeComp)
                dest = Code.dest(codeDest)
                jump = Code.jump(codeJump)

                code = prefix + comp + dest + jump

            print(code + "\n")
            f.write(code + "\n")


def _assemble_code(asm_file):
    parser = Parser(asm_file)

    while parser.hasMoreCommands():
        parser.advance()

        if parser.commandType() == "A_COMMAND":
            assembly = parser.symbol()
            code = AInstruction.encode(assembly)

        if parser.commandType() == "C_COMMAND":
            codeDest = parser.dest()
            codeComp = parser.comp()
            codeJump = parser.jump()

            assm = codeDest, codeComp, codeJump
            print(assm)

            prefix = "111"
            dest = Code.dest(codeDest)
            comp = Code.comp(codeComp)
            jump = Code.jump(codeJump)

            code = prefix + dest + comp + jump

        print(code + "\n")
        print("Hello mum")

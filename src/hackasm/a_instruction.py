class AInstruction:
    def encode(instr):
        intInstr = int(instr)
        prefix = "0"
        binaryInt = "{0:015b}".format(intInstr)
        return prefix + binaryInt

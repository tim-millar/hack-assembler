class AInstruction:
    def encode(instr):
        intInstr = int(instr)
        binaryInt = "{0:016b}".format(intInstr)
        return binaryInt

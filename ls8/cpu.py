"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.running = True

        # instruction handlers
        self.HLT = 0b00000001
        self.LDI = 0b10000010
        self.PRN = 0b01000111

    def ram_read(self, MAR):
        return self.ram[MAR]
    
    def ram_write(self, MAR, MDR):
        self.ram[MAR] =  MDR


    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # 0b prefix denotes binary
            # From print8.ls8
            self.LDI, # LDI R0,8
            0b00000000,
            0b00001000,
            self.PRN, # PRN R0
            0b00000000,
            self.HLT, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # FETCH, DECODE, EXECUTE
        self.trace()

        while self.running:
            IR = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            if IR == "ADD":
                self.alu("ADD", operand_a, operand_b)
                self.pc += 3
            elif IR == self.HLT:
                self.running = False
                self.pc += 1
            elif IR == self.LDI:
                self.reg[operand_a] = operand_b
                self.pc += 3
            elif IR == self.PRN:
                num = self.reg[int(str(operand_a))]
                print(num)
                self.pc += 2
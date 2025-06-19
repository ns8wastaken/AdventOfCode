from common.base_solution import BaseSolution
from concurrent.futures import ProcessPoolExecutor

class Registers:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

class Computer:
    def __init__(self, registers: Registers, program: list[int]):
        self.regs = registers
        self.program = program
        self.pointer = 0

        self.inc_on_next = True

        self.output: list[int] = []

    def compute_next_instruction(self) -> bool:
        opcode = self.program[self.pointer]
        literal_operand = self.program[self.pointer + 1]
        combo_operand = literal_operand
        if   literal_operand == 4: combo_operand = self.regs.a
        elif literal_operand == 5: combo_operand = self.regs.b
        elif literal_operand == 6: combo_operand = self.regs.c
        elif literal_operand == 7: print("[PANIC] The combo operand 7 appeared in the program")

        match opcode:
            case 0:
                self.regs.a = int(self.regs.a / (2 ** combo_operand))

            case 1:
                self.regs.b ^= literal_operand

            case 2:
                self.regs.b = combo_operand % 8

            case 3:
                if self.regs.a != 0:
                    self.inc_on_next = False
                    self.pointer = literal_operand

            case 4:
                self.regs.b ^= self.regs.c

            case 5:
                self.output.append(combo_operand % 8)

            case 6:
                self.regs.b = int(self.regs.a / (2 ** combo_operand))

            case 7:
                self.regs.c = int(self.regs.a / (2 ** combo_operand))

        if self.inc_on_next:
            self.pointer += 2
        self.inc_on_next = True

        if self.pointer >= len(self.program):
            return False

        return True

    def reset(self):
        self.regs.a = 0
        self.regs.b = 0
        self.regs.c = 0
        self.output.clear()
        self.pointer = 0

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        regs = Registers()
        program = []

        for l in self.dataRaw.split('\n'):
            if l.startswith("Register"):
                reg = l[9]
                n = int(l[12:])

                if   reg == 'A': regs.a = n
                elif reg == 'B': regs.b = n
                elif reg == 'C': regs.c = n

            elif l.startswith("Program"):
                program = list(map(int, l[9:].split(',')))

        computer = Computer(regs, program)
        while computer.compute_next_instruction():
            pass

        return ','.join(map(str, computer.output))

    def Part2(self) -> BaseSolution.ResultType:
        regs = Registers()
        program = []

        for l in self.dataRaw.split('\n'):
            if l.startswith("Register"):
                reg = l[9]
                n = int(l[12:])

                if   reg == 'A': regs.a = n
                elif reg == 'B': regs.b = n
                elif reg == 'C': regs.c = n

            elif l.startswith("Program"):
                program = list(map(int, l[9:].split(',')))

        computer = Computer(regs, program)

        # computer.regs.a = ?
        #
        # while computer.regs.a != 0:
        #     # b = (a & 7) ^ 1
        #     # b = (b ^ (a // b)) ^ 4
        #     # a = a // 8
        #     # out b & 7
        #     computer.regs.b = (computer.regs.a & 7) ^ 1
        #     computer.regs.b = (computer.regs.b ^ int(computer.regs.a / computer.regs.b)) ^ 4
        #     computer.regs.b ^= 4
        #     computer.regs.a //= 8
        #     computer.output.append(computer.regs.b & 7)

        return None

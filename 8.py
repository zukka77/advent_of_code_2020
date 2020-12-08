import os
from collections import namedtuple

class Computer():
    def __init__(self,program):
        self.program=program
        self.pc=0
        self.acc=0
        self.executed_instructions=set()
        self.infinite_loop=False
        self.done=False
    
    def execute(self):
        while (True):
            if self.pc in self.executed_instructions:
                self.done=True
                self.infinite_loop=True
                return self.acc
            if self.pc >= len(program):
                self.done=True
                return self.acc
            self.executed_instructions.add(self.pc)
            i = self.program[self.pc]
            if i.opcode=='nop':
                self.pc+=1
            elif i.opcode=='acc':
                self.acc+=i.arg
                self.pc+=1
            elif i.opcode=='jmp':
                self.pc+=i.arg
            

Instruction=namedtuple('Instruction',['opcode','arg'])
program=[]
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),__file__.replace('.py','.in')),'r',encoding='utf8') as f:
    for l in f:
        program.append(Instruction(l.split()[0],int(l.split()[1])))

c=Computer(program)
print(c.execute())
print(c.infinite_loop)
for i in range(len(program)):
    if program[i].opcode=='acc':
        continue
    new_program=list(program)
    if program[i].opcode=='jmp':
        new_program[i]=Instruction('nop',program[i].arg)
    else:
        new_program[i]=Instruction('jmp',program[i].arg)
    c=Computer(new_program)
    res=c.execute()
    if not c.infinite_loop:
        print (res)
        break

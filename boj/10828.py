import sys
from typing import List


class Stack:
    def __init__(self, arr: List=[]):
        self.stack = arr
    
    def push(self, x: int):
        self.stack.append(x)
    
    def pop(self):
        try:
            print(self.stack.pop())
        except IndexError:
            print(-1)
    
    def size(self):
        print(len(self.stack))
    
    def empty(self):
        if self.stack:
            print(0)
        else:
            print(1)
    
    def top(self):
        try:
            print(self.stack[-1])
        except IndexError:
            print(-1)


N = int(sys.stdin.readline())
commands = [line.rstrip() for line in sys.stdin.readlines()]
stack = Stack()

for command in commands:
    command = command.split(" ")
    if len(command) == 1:
        getattr(stack, command[0])()
    else:
        getattr(stack, command[0])(int(command[1]))

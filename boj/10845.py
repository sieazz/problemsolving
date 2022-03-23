import sys
from collections import deque
from typing import List


class Queue:
    def __init__(self, arr: List=[]):
        self.queue = deque(arr)
    
    def push(self, x: int):
        self.queue.append(x)
    
    def pop(self):
        try:
            print(self.queue.popleft())
        except IndexError:
            print(-1)
    
    def size(self):
        print(len(self.queue))
    
    def empty(self):
        if self.queue:
            print(0)
        else:
            print(1)
    
    def front(self):
        try:
            print(self.queue[0])
        except IndexError:
            print(-1)
    
    def back(self):
        try:
            print(self.queue[-1])
        except IndexError:
            print(-1)


N = int(sys.stdin.readline())
commands = [line.rstrip() for line in sys.stdin.readlines()]
queue = Queue()

for command in commands:
    command = command.split(" ")
    if len(command) == 1:
        getattr(queue, command[0])()
    else:
        getattr(queue, command[0])(int(command[1]))

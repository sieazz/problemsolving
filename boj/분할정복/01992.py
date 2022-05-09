import sys
from typing import List


N = int(sys.stdin.readline())
pic = [list(line.rstrip()) for line in sys.stdin.readlines()]
result = []


def compress(N: int, x: int, y: int):
    pixel = pic[x][y]
    pixel_equivalent = True
    for i in range(N):
        if not pixel_equivalent:
            break
        for j in range(N):
            if pic[x+i][y+j] != pixel:
                pixel_equivalent = False
                result.append('(')
                compress(N//2, x, y)
                compress(N//2, x, y+N//2)
                compress(N//2, x+N//2, y)
                compress(N//2, x+N//2, y+N//2)
                result.append(')')
                break
    
    if pixel_equivalent:
        result.append(pixel)


compress(N, 0, 0)
print("".join(result))
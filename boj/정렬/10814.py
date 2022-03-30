import sys

# lambda식을 sorted의 인자로 사용했을 때의 활용예

N = int(sys.stdin.readline().rstrip())
num = [[int(x_y.split(" ")[0]), x_y.split(" ")[1:].rstrip()] for x_y in sys.stdin.readlines()]

# The sort is stable – if two items have the same key, their order will be preserved in the sorted list.
for x, y in sorted(num, key= lambda x:x[0]): 
	print(f"{x} {y}")
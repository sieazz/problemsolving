import sys

# lambda식을 sorted의 인자로 사용했을 때의 활용예

N = int(sys.stdin.readline().rstrip())
num = [[line.split(" ")[0], *list(map(int, line.split(" ")[1:]))] for line in sys.stdin.readlines()]

# lambda x:(x[0],x[1]): x[0], x[1] 순서대로 각각 ascending하게 정렬
# lambda x:(-x[1],x[0]): x[1], x[0] 순서대로 각각 descending, ascending하게 정렬
for line in sorted(num, key= lambda x:(-x[1], x[2], -x[3], x[0])): 
	print(line[0])
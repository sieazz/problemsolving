import sys
from typing import List

# merge sort
# merging하면서 iterator를 사용
# 두 array를 더하면 새로운 array를 생성하므로 pointer에 대한 지나친 고민이 필요 없음

N = int(sys.stdin.readline().rstrip())
num = [int(i) for i in sys.stdin.readlines()]

def merge(arr1, arr2: List) -> List:
	arr = []
	iter1, iter2 = iter(arr1), iter(arr2)

	move = 0

	while True:
		try:
			if move != 2:
				val1 = next(iter1)
		except StopIteration:
			arr.append(val2)
			for val2 in iter2:
				arr.append(val2)
			break
		try:
			if move != 1:
				val2 = next(iter2)
		except StopIteration:
			arr.append(val1)
			for val1 in iter1:
				arr.append(val1)
			break
		if val1 < val2:
			arr.append(val1)
			move = 1
		else:
			arr.append(val2)
			move = 2
	return arr


# 두 부분 array의 길이가 모두 0이 되도록 분할하는 경우는 없다
def merge_sort(arr: List) -> List:
	if len(arr) == 1:
		return arr

	index = len(arr)//2
	arr1 = merge_sort(arr[:index])
	arr2 = merge_sort(arr[index:])
	return merge(arr1, arr2)

for i in merge_sort(num):
	print(i)
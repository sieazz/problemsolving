import sys
from typing import List


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))


# A[a_n]에서 i<j 일때 a_i>a_j의 개수 = merge sort에서의 교차점 개수
# merge과정에서 뒤에 있는 부분배열의 element가 앞에 있는 부분배열의 element보다 작을 때 교차점 발생
def find_intersection(start, end: int, array: List) -> int:
    if start+1 == end:
        return 0
    
    num_inter_sub1 = find_intersection(start, (start+end)//2, array)
    num_inter_sub2 = find_intersection((start+end)//2, end, array)
    num_inter = 0

    subarray1 = list(reversed(array[start:(start+end)//2]))
    subarray2 = list(reversed(array[(start+end)//2:end]))
    i = start
    while subarray1 and subarray2:
        if subarray1[-1] > subarray2[-1]:
            num_inter += len(subarray1)
            array[i] = subarray2.pop()
        else:
            array[i] = subarray1.pop()
        i += 1
    
    while subarray1:
        array[i] = subarray1.pop()
        i += 1
    while subarray2:
        array[i] = subarray2.pop()
        i += 1
    
    return num_inter + num_inter_sub1 + num_inter_sub2


print(find_intersection(0, N, A))


import time
import sys


def multiply(nums: list):
    ans = 1
    for num in nums:
        if num == 0:
            return 0
        ans *= num
    return ans


def find_max_product(table: list, len_adj: list) -> int:
    max_val = -sys.maxsize

    # left-right
    for i in range(len(table)):
        for j in range(len(table)-(len_adj-1)):
            adj_list = table[i][j:j+len_adj]
            mul_res = multiply(adj_list)
            if max_val < mul_res:
                max_val = mul_res

    # up-down
    for i in range(len(table)):
        for j in range(len(table)-(len_adj-1)):
            adj_list = []
            for k in range(len_adj):
                adj_list.append(table[j+k][i])
            mul_res = multiply(adj_list)
            if max_val < mul_res:
                max_val = mul_res

    # diagonal(left,up -> right,down)
    for i in range(len(table)-(len_adj-1)):
        for j in range(len(table)-(len_adj-1)):
            adj_list = []
            for k in range(len_adj):
                adj_list.append(table[i+k][j+k])
            mul_res = multiply(adj_list)
            if max_val < mul_res:
                max_val = mul_res

    # diagonal(left,down -> right,up)
    for i in range(len(table)-(len_adj-1)):
        for j in range(len(table)-(len_adj-1)):
            adj_list = []
            for k in range(len_adj):
                adj_list.append(table[i+len_adj-1-k][j+k])
            mul_res = multiply(adj_list)
            if max_val < mul_res:
                max_val = mul_res

    return max_val


start = time.time()

table = []

with open('input_files/011.txt', 'r') as f:
    while True:
        row = f.readline().strip()
        if len(row) == 0:
            break
        table.append([int(i) for i in row.split()])

print(find_max_product(table, 4))

end = time.time()
print('time spent: {:.3f}'.format(end-start))

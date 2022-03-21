from collections import defaultdict
import time


start = time.time()

print('The number under N which produces longest collatz sequence')
N = int(input('Enter N: '))

chain_len_list = defaultdict(int)

for i in range(1, N):
    n = i
    chain_len = 1
    chain_path = []
    while n != 1:
        if n in chain_len_list.keys():
            chain_len += chain_len_list[n] - 1
            break
        else:
            chain_len += 1
            chain_path.append(n)
            if n & 1:
                n = 3*n + 1
            else:
                n = (int)(n/2)

    for i in range(len(chain_path)):
        chain_len_list[chain_path[i]] = chain_len - i

max_key = 0
max_value = 0
for key, value in chain_len_list.items():
    if max_value < value:
        max_key = key
        max_value = value

print(max_key)

end = time.time()
print('time spent: {:.3f}'.format(end-start))

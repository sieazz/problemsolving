import time
from math_snippets.divisor import find_divisors


print('The first triangule number over N divisors')
N = int(input('Enter N: '))

start = time.time()
tri_num = 0
i = 1
while True:
    tri_num += i
    if len(find_divisors(tri_num)) > N:
        break
    i += 1

print(tri_num)

end = time.time()
print('time spent: {:.3f}'.format(end-start))

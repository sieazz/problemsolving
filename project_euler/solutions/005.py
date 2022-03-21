import collections
import time
from math_snippets import prime_factorization as pf


start = time.time()

print('A smallest number which can be divided by each of the numbers from 1 to N')
N = int(input('Enter N: '))

start = time.time()
pf_num = {}

# Find the prime factors and their each minimum number
# to be able to divided by 1~N
for i in reversed(range(int(N ** 0.5)+1, N+1)):
    factors = collections.Counter(pf.find_prime_factors(i))
    for base, exp in factors.items():
        try:
            if exp > pf_num[base]:
                pf_num[base] = exp
        except KeyError:
            pf_num[base] = exp

# Calculate
ans = 1
for base, exp in pf_num.items():
    ans *= (base ** exp)
print(ans)

end = time.time()
print('time spent: {:.3f}'.format(end-start))

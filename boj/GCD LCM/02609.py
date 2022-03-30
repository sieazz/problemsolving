import sys


def find_divisors(N: int) -> list:
    divisors = set([1, ])
    if N != 1:
        divisors.add(N)
        for i in range(2, int(N**0.5)+1):
            if N % i == 0:
                divisors.add(i)
                divisors.add(N//i)
    return sorted(list(divisors))


M, N = map(int, sys.stdin.readline().rstrip('\n').split(" "))
M_divisors, N_divisors = find_divisors(M), find_divisors(N)

GCD = max(set(M_divisors) & set(N_divisors))
LCM = (M//GCD)*(N//GCD)*GCD

print(GCD)
print(LCM)
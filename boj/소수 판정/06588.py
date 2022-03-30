import sys


testcases = [int(line) for line in sys.stdin.readlines()]

def find_odd_primes(N):
    sleve = [True]*(N+1)
    sleve[0], sleve[1] = False, False

    for i in range(2, (int)(N**(1/2))+1):
        if sleve[i]:
            j = 2
            while i*j <= N:
                sleve[i*j] = False
                j += 1

    return [i for i in range(3, N//2+1) if sleve[i]]


def is_prime(N):
    if N <= 1:
        return False
    for i in range(2, (int)(N**(1/2))+1):
        if N % i == 0:
            return False
    return True


# 매 testcase를 조사하면서 소수 목록을 생성하면 timeout
odd_primes = find_odd_primes(max(testcases))

for n in testcases:
    if n:
        result = ''
        for prime in odd_primes:
            if is_prime(n-prime):
                result = f"{n} = {prime} + {n-prime}"
                break
        print(result) if result else print("Goldbach's conjecture is wrong.")

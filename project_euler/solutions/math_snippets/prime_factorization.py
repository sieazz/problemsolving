import sleve_eratos as se


def find_prime_factors(N: int) -> list:
    primes = se.find_primes(N+1)
    prime_factors = []
    for i in primes:
        if N % i == 0:
            N = N//i
            prime_factors.append(i)
            while N % i == 0:
                N = N//i
        if N == 1:
            break
    return prime_factors


if __name__ == "__main__":
    N = int(input("Print all prime factors of: "))
    print(find_prime_factors(N))

def find_primes(N: int) -> list:
    sleve = [True] * N
    sleve[0] = False
    for i in range(2, int(N**0.5)):
        if sleve[i]:
            j = 2
            while i*j < N:
                sleve[i*j] = False
                j += 1
    return [i for i in range(2, len(sleve)) if sleve[i]]


if __name__ == "__main__":
    N = int(input("Print all primes less than: "))
    print(find_primes(N))

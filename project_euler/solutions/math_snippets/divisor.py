def find_divisors(N: int) -> list:
    divisors = set([1, ])
    if N != 1:
        divisors.add(N)
        for i in range(2, int(N**0.5)+1):
            if N % i == 0:
                divisors.add(i)
                divisors.add(N//i)
    return sorted(list(divisors))


if __name__ == "__main__":
    N = int(input("Print all divisors of: "))
    print(find_divisor(N))

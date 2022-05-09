def hanoi(src, via, dst, N):
    if N >= 1:
        hanoi(src, dst, via, N-1)
        print(f"{src} {dst}")
        hanoi(via, src, dst, N-1)


N = int(input())
print(2**N-1)
hanoi(1, 2, 3, N)
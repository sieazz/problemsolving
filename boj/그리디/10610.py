N = list(map(int, input()))
if 0 in N and sum(N)%3 == 0:
    N = sorted(N, reverse=True)
    print(int("".join(map(str, N))))
else:
    print(-1)
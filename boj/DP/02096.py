import sys


N = int(sys.stdin.readline())

max_dp = list(map(int, sys.stdin.readline().rstrip().split()))
min_dp = max_dp[::]
for i in range(1, N):
    points = list(map(int, sys.stdin.readline().rstrip().split()))

    max_0 = points[0] + max(max_dp[0], max_dp[1])
    max_1 = points[1] + max(max_dp[0], max_dp[1], max_dp[2])
    max_2 = points[2] + max(max_dp[1], max_dp[2])

    min_0 = points[0] + min(min_dp[0], min_dp[1])
    min_1 = points[1] + min(min_dp[0], min_dp[1], min_dp[2])
    min_2 = points[2] + min(min_dp[1], min_dp[2])

    max_dp = [max_0, max_1, max_2]
    min_dp = [min_0, min_1, min_2]

print(f"{max(max_dp)} {min(min_dp)}")


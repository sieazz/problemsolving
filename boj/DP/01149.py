import sys


N = int(sys.stdin.readline())
price_list = [list(map(int, line.rstrip().split())) for line in sys.stdin.readlines()]
dp = [price_list[0]]

for i in range(1, N):
    red_min = price_list[i][0] + min(dp[i-1][1], dp[i-1][2])
    green_min = price_list[i][1] + min(dp[i-1][0], dp[i-1][2])
    blue_min = price_list[i][2] + min(dp[i-1][0], dp[i-1][1])
    dp.append([red_min, green_min, blue_min])

print(min(dp[-1]))


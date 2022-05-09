N = int(input())
map_star = [[' ']*((N//3)*5+(N//3)-1) for _ in range(N)]

# start: 삼각형의 최상단 별 위치
def construct(size: int, start: tuple):
    # base case
    x, y = start
    print(f"{size} {x} {y}")
    if size == 3:
        map_star[x][y] = '*'
        map_star[x+1][y-1] = '*'
        map_star[x+1][y+1] = '*'
        for i in range(5):
            map_star[x+2][y-2+i] = '*'
    else:
        construct(size//2, (x, y))
        construct(size//2, (x+(size//2), y-(size//2)))
        construct(size//2, (x+(size//2), y+(size//2)))

construct(N, (0, ((N//3)*5+(N//3)-1)//2))
for line in map_star:
    print("".join(line))

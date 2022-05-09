import sys
from typing import List

def sol():
    N = int(sys.stdin.readline())

    paper = [list(map(int, line.rstrip().split())) for line in sys.stdin.readlines()]

    paper_num = [0, 0, 0]


    def check_paper(N: int, start: tuple, paper: List, paper_num: List):
        # 1, 0, -1의 개수를 센다
        num_neg1, num_0, num_1 = 0, 0, 0
        flag = False
        for i in range(N):
            if flag:
                break
            for j in range(N):
                if paper[start[0]+i][start[1]+j] == -1:
                    if num_0 or num_1:
                        flag = True
                        break
                    num_neg1 += 1
                elif paper[start[0]+i][start[1]+j] == 0:
                    if num_neg1 or num_1:
                        flag = True
                        break
                    num_0 += 1
                elif paper[start[0]+i][start[1]+j] == 1:
                    if num_neg1 or num_0:
                        flag = True
                        break
                    num_1 += 1

        # 모두 다 같을 경우 개수 업데이트
        # 다른게 있을 시 9등분한다
        if flag:
            check_paper(N//3, (start[0], start[1]), paper, paper_num)
            check_paper(N//3, (start[0], start[1]+ N//3), paper, paper_num)
            check_paper(N//3, (start[0], start[1]+ 2*N//3), paper, paper_num)
            check_paper(N//3, (start[0] + N//3, start[1]), paper, paper_num)
            check_paper(N//3, (start[0] + N//3, start[1]+ N//3), paper, paper_num)
            check_paper(N//3, (start[0] + N//3, start[1]+ 2*N//3), paper, paper_num)
            check_paper(N//3, (start[0] + 2*N//3, start[1]), paper, paper_num)
            check_paper(N//3, (start[0] + 2*N//3, start[1]+ N//3), paper, paper_num)
            check_paper(N//3, (start[0] + 2*N//3, start[1]+ 2*N//3), paper, paper_num)
        elif num_neg1 == N**2:
            paper_num[0] += 1
        elif num_0 == N**2:
            paper_num[1] += 1
        elif num_1 == N**2:
            paper_num[2] += 1

        
    check_paper(N, (0,0), paper, paper_num)
    [print(num) for num in paper_num]

sol()
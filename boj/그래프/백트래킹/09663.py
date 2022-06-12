def sol():
    N = int(input())

    available_y = [True for _ in range(N)]
    available_diagonal1 = [True for _ in range(2*N-1)]  # ↘
    available_diagonal2 = [True for _ in range(2*N-1)]  # ↗
    case = 0

    def n_queen(row):
        nonlocal case
        if row == N:
            case += 1
            return
        
        for col in range(N):
            if available_y[col] and available_diagonal1[N-1 - (col-row)] and available_diagonal2[row+col]:
                available_y[col], available_diagonal1[N-1 - (col-row)], available_diagonal2[row+col] = False, False, False
                n_queen(row + 1)
                available_y[col], available_diagonal1[N-1 - (col-row)], available_diagonal2[row+col] = True, True, True

    n_queen(0)
    print(case)


sol()
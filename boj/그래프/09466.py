import sys


T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    student_selection = list(map(int, sys.stdin.readline().split(" ")))
    student_selection = [-1] + student_selection

    stack = []
    visited = [False]*(n+1)
    visited[0] = True

    students_without_team = n
    for i in range(1, n+1):
        if not visited[i]:
            path = []
            while not visited[i]:
                path.append(i)
                visited[i] = True
                i = student_selection[i]
            try:
                cycle_start_index = path.index(i)
                cycle_len = len(path) - cycle_start_index
                students_without_team -= cycle_len
            except ValueError:
                pass

    print(students_without_team)



import time


start = time.time()

with open('input_files/067.txt', 'r') as f:
    triangle = [list(map(int, line.rstrip().split())) for line in f.readlines()]

dp = [[triangle[0][0]],]

for line in triangle[1:]:
    dp.append([])
    for i in range(len(line)):
        if i == 0:
            dp[-1].append(dp[-2][0] + line[i])
        elif i == len(line)-1:
            dp[-1].append(dp[-2][-1] + line[i])
        else:
            dp[-1].append(max(dp[-2][i-1], dp[-2][i]) + line[i])

print(max(dp[-1]))


end = time.time()
print('time spent: {:.3f}'.format(end-start))

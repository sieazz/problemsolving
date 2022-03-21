import time


print('Find out a^2+b^2=c^2 which satisfys a+b+c=N and a<b<c')
N = int(input('Enter N: '))

start = time.time()
condition = 1

for a in range(1, N-1):
    if condition == 0:
        break
    sum_of_b_c = N-a
    for b in range(a+1, sum_of_b_c-1):
        c = sum_of_b_c - b
        if a >= b or b >= c:
            break
        if a**2 + b**2 == c**2:
            print(f'a = {a}, b = {b}, c = {c}')
            condition = 0
            break

if condition == 1:
    print('There is no such (a,b,c) satisfys the condition')
end = time.time()
print('time spent: {:.3f}'.format(end-start))

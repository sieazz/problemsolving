import time


start = time.time()

sum = 0
with open('input_files/013.txt', 'r') as f:
    while True:
        num = f.readline()
        if len(num) == 0:
            break
        sum += int(num)

print(str(sum)[0:10])

end = time.time()
print('time spent: {:.3f}'.format(end-start))
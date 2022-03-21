import time


def str_elements_mul(string: str) -> int:
    mul = 1
    for i in string:
        mul *= int(i)
    return mul


start = time.time()


N = 13
text = ""

with open('input_files/008.txt', 'r') as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        text += line.rstrip('\n')

max_mul = -1
for i in range(0, len(text)-(N-1)):
    mul = str_elements_mul(text[i:i+N])
    max_mul = max(max_mul, mul)

print(max_mul)

end = time.time()
print('time spent: {:.3f}'.format(end-start))

import time


def is_palindrome_num(i: int) -> bool:
    number = i
    result = 0
    while number > 0:
        rem = number % 10
        number //= 10
        result = result * 10 + rem

    return i == result


print('Biggest palindromic number made from the product of two N-digit numbers')
N = int(input('Enter N: '))

start = time.time()
pal_num = -1

for i in reversed(range(10**(N-1), 10**N)):
    for j in reversed(range(i, 10**N)):
        number = i*j
        if number < pal_num:
            break
        if number > pal_num and is_palindrome_num(number):
            pal_num = number
            break

print(pal_num)

end = time.time()
print('time spent: {:.3f}'.format(end-start))

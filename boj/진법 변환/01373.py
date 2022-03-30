import sys


num_bin = sys.stdin.readline().rstrip('\n')

# 세자리씩 끊어서 변환
len3_bits = [num_bin[-3:]]
len3_bits += [num_bin[-3*(i+1):-3*i] for i in range(1, (len(num_bin)-1)//3+1)]

num_oct = ''
i=0
for len3_bit in len3_bits:
    bit = 0
    try:
        bit += int(len3_bit[-1]) * (2**0)
        bit += int(len3_bit[-2]) * (2**1)
        bit += int(len3_bit[-3]) * (2**2)
    except IndexError:
        pass
    num_oct = str(bit) + num_oct 
    i += 1

print(num_oct)


# 내장함수 이용, 2진수 -> 10진수 -> 8진수 변환
print(oct(int(num_bin, 2))[2:])
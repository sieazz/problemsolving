import time


print('Difference between' +
      ' the square of the sums and the sum of the squares from 1 to N')
N = int(input('Enter N: '))

start = time.time()

square_of_sums = (N*(N+1)/2)**2
sum_of_squares = (N*(N+1)*(2*N+1))/6

print(int(square_of_sums - sum_of_squares))

end = time.time()
print('time spent: {:.3f}'.format(end-start))

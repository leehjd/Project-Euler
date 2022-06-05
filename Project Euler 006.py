# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def difference(n):
    sum_of_squares = 0
    sum = 0
    for i in range(n+1):
        sum_of_squares += i**2
        sum += i
    square_of_sum = sum**2
    return square_of_sum - sum_of_squares

print(difference(100))
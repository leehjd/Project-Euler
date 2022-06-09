# What is the sum of the digits of the number 2^1000?

def sum_of_digits(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

print(sum_of_digits(2**1000))
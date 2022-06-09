# Find the largest palindrome made from the product of two 3-digit numbers.

palindromes = []
for n in range(100,1000):
    for m in range(100,1000):
        product = n * m
        reverse = int(str(product)[::-1])
        if reverse == product:
            palindromes.append(product)

print(max(palindromes))


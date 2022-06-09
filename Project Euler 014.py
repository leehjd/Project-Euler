greatest = 0
for j in range(1,1000001):
    count = 0
    i = j
    while True:
        if i == 1:
            break
        elif i % 2 == 0:
            i //= 2
            count += 1
        else:
            i = 3*i + 1
            count += 1
    if count > greatest:
        greatest = count
        which = j

print(which)
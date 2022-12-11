nos = [3, 1, -2, 4, -1, 2, 5]
total = 0
even_sum = 0
odd_sum = 0
for x in nos:
    if x > 0:
        total += x
        if x % 2 == 0:
            even_sum += x
        else:
            odd_sum += x

print(total, even_sum, odd_sum)



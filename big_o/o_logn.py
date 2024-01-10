def number_of_bits(n):
    count = 0
    while n > 0:
        n = n // 2
        count += 1
    return count


print(number_of_bits(8))

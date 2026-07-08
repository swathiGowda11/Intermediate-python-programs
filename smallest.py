def smallest_dig(num):
    smallest = num % 10
    num = num // 10
    while num > 0:
        digit = num % 10
        if digit < smallest:
            smallest = digit
        num = num // 10
    return smallest
result = smallest_dig(58392)
print(result)
def largest_digit(num):
    largest = 0

    while num > 0:
        digit = num % 10

        if digit > largest:
            largest = digit

        num = num // 10

    return largest

result = largest_digit(58392)
print(result)
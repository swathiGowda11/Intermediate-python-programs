def strong(num):
    original_num = num
    total = 0
    current_num = num
    while current_num > 0:
        digit = current_num % 10
        factorial = 1

        for i in range(1, digit + 1):
            factorial *= i

        total += factorial
        current_num //= 10

    if total == original_num:
        return "strong"
    else:
        return "not strong"


result = strong(145)
print(result)


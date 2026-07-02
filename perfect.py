def perfect(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if total == num:
        return "perfect"
    else:
        return "not perfect"
result = perfect(6)
print(result)
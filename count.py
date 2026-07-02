'''count numbers'''
def count_numbers(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count
result = count_numbers(2486)
print(result)

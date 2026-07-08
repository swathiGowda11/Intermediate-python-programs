def lcm(a, b):
    multiple = max(a, b)

    while True:
        if multiple % a == 0 and multiple % b == 0:
            return multiple
        multiple += 1


result = lcm(12, 18)
print(result)


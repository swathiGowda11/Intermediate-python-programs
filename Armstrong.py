num = 153
def armstrong(num):
    original_num = num
    count = 0
    temp = num
    while temp > 0:
        count += 1
        temp = temp//10
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** count
        temp //= 10
    if total == original_num:
        return "Armstrong"
    else:
        return "Not Armstrong"

if __name__ == "__main__":
    print(armstrong(num))


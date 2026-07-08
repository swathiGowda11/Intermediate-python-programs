'''greatest common divisor'''

def gcd(a,b):
    gcd = 1
    for i in range(1,min(a,b)+1):
        if a % i ==0 and b% i ==0:
            gcd = i
    return gcd
result = gcd(12,18)
print(result)




'''solution1:'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(gcd(12, 18))
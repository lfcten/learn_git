# gcd_Euclid
def gcd(a, b):
    while b:
        a, b = b, a % b
    return b
    
# gdc_Stein
def gcd_stein(a, b):
    if not (a % 2 or b % 2):
        return 2 * gcd_stein(a >> 1, b >> 1)
    elif not a % 2:
        return gcd_stein(a >> 1, b)
    elif not b % 2:
        return gcd_stein(a, b >> 1)
    else:
        return gcd_stein(abs(a - b), min(a, b))

# 拓展欧几里得
def extend_gcd(a, b):
    global x, y
    if b == 0:
        x = 1
        y = 0
        return a

    r = extend_gcd(b, a % b)

    x, y = y, x - (a // b) * y
    return r

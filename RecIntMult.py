# recursive multiplier using divide-and-conquer that works for two n-digit integers where n is a power of 2
# look at Karatsuba!!! optimized version of this
def RecIntMult(x, y, n):
    if n == 1: return x * y
    n_halved = n//2
    # x = a * 10^(n/2) + b where a is the first half of digits and b is the second half
    a, b = x // pow(10, n_halved), x % pow(10, n_halved)
    c, d = y // pow(10, n_halved), y % pow(10, n_halved)
    # do binomial multiplication using FOIL method (first, inner, outer, last)
    ac, ad = RecIntMult(a, c, n_halved), RecIntMult(a, d, n_halved)
    bc, bd = RecIntMult(b, c, n_halved), RecIntMult(b, d, n_halved)
    return pow(10, n) * ac + pow(10, n_halved) * (ad + bc) + bd
# Time Complexity: O(n^2)
# 4 recursive calls + work done in each call
# T(n) = 4T(n/2) + O(n^1) <- n cuz pow, div, mod are O(n) operations
# a = 4, b = 2, d = 1
# using master theorem, since a > b^d: time complexity is O(n^log_2(4)) = O(n^2)

# Space Complexity: O(log(n))
# function call stack goes up to log(n)

x = 1234
y = 5678
n = 4
print(RecIntMult(x, y, n))
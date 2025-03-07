# look at RecIntMult first!!!
# this is an optimized version of that works with any n

def Karatsuba(x, y):
    if x < 10 and y < 10: return x * y
    n_halved = max(len(str(x)), len(str(y)))//2
    a, b = divmod(x, 10**n_halved)
    c, d = divmod(y, 10**n_halved)
    p, q = a + b, c + d
    ac, bd = Karatsuba(a, c), Karatsuba(b, d)
    pq = Karatsuba(p, q) # pq = ac + bc + ad + bd
    return pow(10, n_halved*2) * ac + pow(10, n_halved) * (pq - ac - bd) + bd
# Time Complexity: O(n^log_2(3)) = O(n^1.585)
# 3 recursive calls instead of 4

# Space Complexity: O(log(n))

x = 1234
y = 5678
print(Karatsuba(x, y))

x = 123
y = 567
print(Karatsuba(x, y))
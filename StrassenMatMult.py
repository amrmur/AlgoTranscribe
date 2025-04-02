import numpy as np

def strassen(arr, arr2):
    n = len(arr)
    if n == 1: return np.array([[arr[0][0] * arr2[0][0]]])

    A, B, C, D = arr[:n//2, :n//2], arr[:n//2, n//2:], arr[n//2:, :n//2], arr[n//2:, n//2:]
    E, F, G, H = arr2[:n//2, :n//2], arr2[:n//2, n//2:], arr2[n//2:, :n//2], arr2[n//2:, n//2:]

    rec1 = strassen(A, F-H)
    rec2 = strassen(A+B, H)
    rec3 = strassen(C+D, E)
    rec4 = strassen(D, G-E)
    rec5 = strassen(A+D, E+H)
    rec6 = strassen(B-D, G+H)
    rec7 = strassen(A-C, E+F)

    ans = np.zeros((n, n))
    ans[:n//2, :n//2] = rec5 + rec4 - rec2 + rec6
    ans[:n//2, n//2:] = rec1 + rec2
    ans[n//2:, :n//2] = rec3 + rec4
    ans[n//2:, n//2:] = rec1 + rec5 - rec3 - rec7
    return ans

n = 4
# arr = [[0 for _ in range(n)]for _ in range(n)]
arr = np.array([[0,1,2,3],[4,5,6,7], [4,5,6,7], [4,5,6,7]])
arr2 = np.array([[9,1,2,3],[4,8,6,7], [1,5,6,7], [4,5,3,2]])

print(strassen(arr, arr2))

# Space complexity: O(n^2log(n)) can be reduced to n^2 
# Time Complexity: O(n^(log_2(7))) master's theorem
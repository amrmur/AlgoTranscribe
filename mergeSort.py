def mergeSort(nums):
    n = len(nums)
    if n <= 1: return nums

    half = n//2
    first, second = mergeSort(nums[:half]), mergeSort(nums[half:])
    
    f, s, lens, lenf = 0, 0, len(second), len(first)
    for i in range(0, n):
        if s >= lens or f < lenf and first[f] < second[s]:
            nums[i] = first[f]
            f += 1
        else:
            nums[i] = second[s]
            s += 1
    return nums

nums = [5,2,7,9,3,5,1,7,8,4,2,5]
nums = mergeSort(nums)
print(nums)

# Time Complexity: O(nlogn)
# T(n) = 2T(n/2) + O(n)
# a = 2, b = 2, d = 1
# a = b^d
# Space Complexity: O(n)
# total # of auxillary array length is n (call stack is log_2(n): n/2 + n/4 + n/8 is approx. n)
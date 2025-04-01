# an inversion is when a bigger number is behind a smaller number
# this counts the number of those that have occured

def mergeSort(nums):
    n = len(nums)
    if n <= 1: return nums, 0

    half = n//2
    first, firstInv = mergeSort(nums[:half])
    second, secInv = mergeSort(nums[half:])
    
    inv = firstInv + secInv
    f, s, lens, lenf = 0, 0, len(second), len(first)
    for i in range(0, n):
        if s >= lens or f < lenf and first[f] <= second[s]:
            nums[i] = first[f]
            f += 1
        else:
            inv += lenf - f # ahead of this many numbers in the first half
            nums[i] = second[s]
            s += 1
    return nums, inv

nums = [5,2,7,4,9,3,1,0]
# 2 4 5 7     0 1 3 9
nums, inversions = mergeSort(nums)
print(inversions)

# same as complexity as merge sort

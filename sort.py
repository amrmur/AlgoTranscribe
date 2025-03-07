def selectionSort(nums):
    n = len(nums)
    for i in range(n):
        low = i
        for j in range(i + 1, n):
            if nums[j] < nums[low]:
                low = j
        temp = nums[low]
        nums[low] = nums[i]
        nums[i] = temp
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def insertionSort(nums):
    n = len(nums)
    for i in range(1, n):
        j = i
        while j > 0 and nums[j] < nums[j-1]:
            temp = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = temp
            j -= 1
# Time Complexity: O(n^2) best case is O(n)
# Space Complexity: O(1)

def bubbleSort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(1, n - i): 
            if nums[j] < nums[j-1]:
                temp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = temp
                swapped = True
        if not swapped: break
# Same complexity as insertion
# takes num out unsorted while selection takes num into sorted

arr = [7,2,5,8,9,5,1,3,4]
arr2 = [7,2,5,8,9,5,1,3,4]
arr3 = [7,2,5,8,9,5,1,3,4]
selectionSort(arr)
insertionSort(arr2)
bubbleSort(arr3)
print(arr)
print(arr2)
print(arr3)
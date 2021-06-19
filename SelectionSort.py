'''
Selection Sort

Given an array A

for i = 1 to A.length - 1
    // select the minimum value from unsorted array A[i..A.length]
    smallest_idx = i
    j = i + 1
    while j < A.length
        if A[j] < A[smallest_idx]
            smallest_idx = j
        j = j + 1
    
    // swap the minimum value with the first value of unsorted array A[i..A.length]
    temp = A[i]
    A[i] = A[smallest_idx]
    A[smallest_idx] = temp
'''

class SelectionSort:
    
    def sort(self, nums):
        for i in range(len(nums) - 1):
            min_idx = i

            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j

            nums[i], nums[min_idx] = nums[min_idx], nums[i]

obj = SelectionSort()
nums = [5,2,4,6,1,3]
print(nums)
obj.sort(nums)
print(nums)
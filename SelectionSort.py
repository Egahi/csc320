'''
Selection Sort

Given an array A

SelectionSort(A)
    n = A.length
    for i = 1 to n - 1
        smallest = i
        for j = i + 1 to n
            if A[j] < A[smallest]
                smallest = j
        
        exchange A[i] with A[smallest]


Runtime:
Best case -> O(n^2)
Worst case -> O(n^2)
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
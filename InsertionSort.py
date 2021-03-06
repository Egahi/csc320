'''
Insertion Sort

Given an array, A

InsertionSort(A)
    for i = 2 to A.length
        key = a[i]
        // insert key into sorted array A[1..i-1]
        j = i - 1
        while j > 0 and A[j] > key
            A[j + 1] = A[j]
            j = j - 1

        A[j + 1] = key


Runtime:
Best case -> O(n)
Worst case -> O(n^2)
'''

class InsertionSort:

    def sort_ascending(self, nums):
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i - 1

            while j >= 0 and nums[j] > temp:
                nums[j + 1] = nums[j]
                j -= 1
            
            nums[j + 1] = temp

    def sort_asc_recursively(self, nums):
        if not nums or len(nums) <= 1:
            return

        self.sort_asc_recursively(nums[:-1])

        temp = nums[-1]
        idx = len(nums) - 2
        while idx >= 0 and nums[idx] > temp:
            nums[idx + 1] = nums[idx]
            idx -= 1
        
        nums[idx + 1] = temp
    
    def sort_descending(self, nums):
        for i in reversed(range(0, len(nums) - 1)):
            temp = nums[i]
            j = i + 1

            while j < len(nums) and nums[j] > temp:
                nums[j - 1] = nums[j]
                j += 1
            
            nums[j - 1] = temp

obj = InsertionSort()
nums = [5,2,4,6,1,3]
print(nums)
print('Sorted in ascending order')
obj.sort_ascending(nums)
print(nums)
print('Sorted recursively in ascending order')
obj.sort_asc_recursively(nums)
print(nums)
print('Sorted in descending order')
obj.sort_descending(nums)
print(nums)

'''
Insertion Sort
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
print('Sorted in ascending order')
obj.sort_ascending(nums)
print(nums)
print('Sorted in descending order')
obj.sort_descending(nums)
print(nums)

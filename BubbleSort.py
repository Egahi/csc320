'''
Bubble Sort

Given an array A

for i = 1 to A.length
    isSorted = True

    // compare and order adjancent values of unsorted Array A[0..A.length-i]
    for j = 1 to A.length - i
        if A[j] > A[j+1]
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
            isSorted = False

    // if array is sorted, break loop
    if isSorted
        break
'''

class BubbleSort:

    def sort(self, nums):
        for i in range(len(nums)):
            isSorted = True
            for j in range(len(nums) - (i + 1)):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    isSorted = False

            if isSorted:
                break


obj = BubbleSort()
nums = [5,2,4,6,1,3]
print(nums)
obj.sort(nums)
print(nums)
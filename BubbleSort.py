'''
Bubble Sort

Given an array A

BubbleSort(A)
    n = A.length
    for i = 1 to n
        // compare and order adjacent values of unsorted Array A[1..n-i]
        for j = 1 to n - i
            if A[j] > A[j + 1]
                exchange A[j] with A[j + 1]

        if array is sorted
            break loop


Runtime:
Best case -> O(n)
Worst case -> O(n^2)
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
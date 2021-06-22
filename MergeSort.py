'''
Merge Sort

Given an array A

Merge(A, start, mid, end)
    n1 = mid - start + 1
    n2 = end - mid

    Let L = [1..n1 + 1] and R = [1..n2 + 1] be new arrays

    for i = 1 to n1
        L[i] = A[start + i - 1]

    for j = 1 to n2
        R[i] = A[mid + i]

    L[n1 + 1] = infinity
    R[n2 + 1] = infinity

    i = 1
    j = 1
    for k = start to end
        if L[i] <= R[j]
            A[start + k] = L[i]
            i = i + 1
        else
            A[start + k] = R[j]
            j = j + 1

MergeSort(A, start, end)
    if start < end
        mid = start + (end - start) / 2
        MergeSort(A, start, mid)
        MergeSort(A, mid + 1, end)
        Merge(A, start, mid, end)

Runtime:
Best case -> O(nlgn)
Worst case -> O(nlgn)
'''

class MergeSort:

    def sort(self, nums, start, end):
        if start < end:
            mid = start + (end - start) // 2

            self.sort(nums, start, mid)
            self.sort(nums, mid + 1, end)
            self.merge(nums, start, mid, end)

    def merge(self, nums, start, mid, end):
        n1 = mid - start + 1
        n2 = end - mid

        L = []
        for i in range(n1):
            L.append(nums[start + i])
        L.append(float('inf'))
        
        R = []
        for i in range(n2):
            R.append(nums[mid + i + 1])
        R.append(float('inf'))
        
        left = right = 0
        for i in range(start, end  + 1):
            if L[left] <= R[right]:
                nums[i] = L[left]
                left += 1
            else:
                nums[i] = R[right]
                right += 1

obj = MergeSort()
nums = [5,2,4,6,1,3]
print(nums)
obj.sort(nums, 0, len(nums) - 1)
print(nums)
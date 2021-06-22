'''
Binary Search

Given a sorted array A, to search for an element, key. 
Return the index of the key if found, otherwise return -1

Search(A, key, left, right)
    if left > right
        return -1

    mid_point = left + (right - left) / 2

    if A[mid_point] == key
        return mid_point
    else if A[mid_point] > key
        return Search(A, key, left, mid_point - 1)
    else
        return Search(A, key, mid_point + 1, right)


Runtime:
Best case -> O(1)
Worst case -> O(lgn)
'''

class BinarySearch:

    def search(self, nums, key, left, right):
        if left > right:
            return -1
        
        mid = left + (right - left) // 2

        if nums[mid] == key:
            return mid
        elif nums[mid] > key:
            return self.search(nums, key, left, mid - 1)
        else:
            return self.search(nums, key, mid + 1, right)


obj = BinarySearch()
nums = [1,2,3,4,5,6]
key = 4
print(obj.search(nums, key, 0, len(nums) - 1))
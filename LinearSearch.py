'''
Linear Search

Given an array A, to search for an element, key. 
Return the index of the key if found, otherwise return -1

for i = 1 to A.length
    if A[i] == key
        return i

return -1

'''

class LinearSearch:

    def search(self, nums, key):
        for i in range(len(nums)):
            if nums[i] == key:
                return i

        return -1


obj = LinearSearch()
nums = [5,2,4,6,1,3]
key = 4
print(obj.search(nums, key))
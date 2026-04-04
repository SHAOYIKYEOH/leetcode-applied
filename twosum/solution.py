
class Solution():
    def twoSum(self, nums, target):
        storage = {}
        for i, numbers in enumerate(nums):
            complement = target - numbers
            if complement in storage:
                return (storage[complement], i)
            storage[numbers] = i
        return None

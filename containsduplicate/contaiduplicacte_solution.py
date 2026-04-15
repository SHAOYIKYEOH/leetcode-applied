from typing import List

#solution_1
def containsDuplicate(nums: List[int]) :
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

#solution_2
def containsDuplicate2(nums:List[int]):
    seen =set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False


box = [1,2,3,4,1]

print(containsDuplicate(box))

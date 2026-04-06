## solution
class Solution():
    def twoSum(self, nums, target):
        storage = {}
        for i, numbers in enumerate(nums):
            complement = target - numbers
            if complement in storage:
                return (storage[complement], i)
            storage[numbers] = i
        return None


## applied
def shopping_list(product_dic, budget):
    best_two = []
    best_total = 0

    ## convert it into a list so it looks like
    ## [('apple',10),('banana',20)]
    ##     0             1
    items_list = list(product_dic.items())

    ## use range to give i an index
    for i in range(len(items_list)):
        for i2 in range(i+1, len(items_list)): ## start from i+1
            name1, price1 = items_list[i] ## unpacking
            name2, price2 = items_list[i2]
            total = price1 + price2

            if total <= budget and total > best_total: ## keep updating
                best_total = total
                best_two = [name1, name2]

    return best_two

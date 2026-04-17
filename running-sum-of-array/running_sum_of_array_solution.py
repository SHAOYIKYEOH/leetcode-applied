#solution
def running_sum(nums:list[int]):
    output=[]
    for i in range (len(nums)):
        if i == 0:
            output.append(nums[i])
        else:
            output.append(nums[i]+output[i-1])
    return output            

def weekly_step_progress(nums:list[int]):
    output=[]
    for i in range (len(nums)):
        if i == 0:
            output.append(nums[i])
        else:
            output.append(nums[i]+output[i-1])    
    return output        
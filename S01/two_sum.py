def two_sum(nums, target):
    seen = {}
    for i,num in enumerate(nums):
        a = target - num
        if a in seen:
            return [seen[a],i]
        else :
            seen[num] = i
        


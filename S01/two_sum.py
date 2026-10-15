def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        a = target - num
        if a in seen:
            return [seen[a], i]
        seen[num] = i

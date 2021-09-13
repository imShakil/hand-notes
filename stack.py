def two_sum(nums: list, target: int):
    container = {}

    for i, num in enumerate(nums):
        if target - num in container:
            return [container[target - num], i]
        container[num] = i
    return


print(two_sum([2, 7, 11, 15], 9))

def find_duplicate(nums):
    """Faça o código aqui."""
    if not nums or nums == []:
        return False
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] and nums[i] > 0:
            return nums[i]
    return False

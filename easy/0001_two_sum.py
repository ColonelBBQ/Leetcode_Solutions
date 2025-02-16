class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            n0 = nums[i]
            for j in range(i+1, n):
                n1 = nums[j]
                if n0 + n1 == target:
                    return i, j

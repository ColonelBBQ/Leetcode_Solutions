class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0

        for i in range(len(nums)):
            if nums[k] == 0:
                nums.append(0)
                nums.pop(k)
            else:
                k += 1


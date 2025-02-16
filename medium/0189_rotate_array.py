class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k =  k % n

        for i in range(0, n-k):
            nums.append(nums[i])

        del nums[:n-k]

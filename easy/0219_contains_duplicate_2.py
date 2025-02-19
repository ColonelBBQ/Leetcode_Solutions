class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        nums_dict = dict()
        
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = list()
            nums_dict[nums[i]].append(i)
        
        for key, indices in nums_dict.items():
            for j in range(1, len(indices)):
                if indices[j] - indices[j-1] <= k:
                    return True

        return False           
                
    

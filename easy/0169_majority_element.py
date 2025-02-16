class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = dict()
        max_count = 0
        max_element = 0

        for num in nums:
            if num not in elements:
                elements[num] = []
            elements[num].append(1)
            
        for key, list_count in elements.items():
            count = len(list_count)
            if count > max_count:
                max_count = count
                max_element = key
        return max_element          

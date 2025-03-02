class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = {}

        for item in arr:
            if item not in hash_map:
                hash_map[item] = 0
                hash_map[item] += 1
            else:
                hash_map[item] += 1
        
        values_list = list(hash_map.values())

        return len(values_list) == len(set(values_list))

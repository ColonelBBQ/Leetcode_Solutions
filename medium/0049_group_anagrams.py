class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index_sorted = {}
        answer = []

        for i in range(len(strs)):
            sorted_string = "".join(sorted(strs[i]))
            if sorted_string not in index_sorted:
                index_sorted[sorted_string] = []
            index_sorted[sorted_string].append(i)

        for values in index_sorted.values():
            inner_list = []
            for value in values:
                inner_list.append(strs[value])
            answer.append(inner_list)

        return answer
        

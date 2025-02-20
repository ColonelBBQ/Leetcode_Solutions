class Solution:
    def romanToInt(self, s: str) -> int:
        s_list = list(s)
        n = len(s_list)
        int_list = []

        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        for i in range(0, len(s_list) - 1):
            if mapping[s_list[i]] < mapping[s_list[i + 1]]:
                int_list.append(-mapping[s_list[i]])
            else:
                int_list.append(mapping[s_list[i]])

        int_list.append(mapping[s_list[len(s_list) - 1]])

        return sum(int_list)

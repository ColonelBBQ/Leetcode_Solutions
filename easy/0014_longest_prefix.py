class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_string = strs[0]
        first_string_letters = list(first_string)
        curr_count = 0
        total_count = len(first_string)

        for string in strs[1:]:
            current_string_letters = list(string)
            print("Analysizing string: ", current_string_letters)

            curr_count = 0
            for i in range(0, min(len(first_string_letters), len(current_string_letters))):
                print(current_string_letters[i], first_string_letters[i])
                if current_string_letters[i] == first_string_letters[i]:
                    curr_count += 1
                else:
                    break
                    
            total_count = min(total_count, curr_count)
            print(curr_count)


        print("total count final: ", total_count)

        prefix = "".join(first_string_letters[:total_count])
        return prefix

                

            



        

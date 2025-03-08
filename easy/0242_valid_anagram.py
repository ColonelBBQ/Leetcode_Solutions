class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_map_s = dict()
        hash_map_t = dict()

        for letter_s in s:
            hash_map_s[letter_s] = 1 + hash_map_s.get(letter_s, 0)

        for letter_t in t:
            hash_map_t[letter_t] = 1 + hash_map_t.get(letter_t, 0)

        print(hash_map_s)
        print(hash_map_t)


        for key, value in hash_map_s.items():
            print(key, value)
            print(hash_map_t.get(letter_t, 0))
            if hash_map_s[key] != hash_map_t.get(key, 0):
                return False
        
        return True

        



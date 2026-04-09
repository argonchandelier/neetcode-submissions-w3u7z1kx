class Solution:
    def convert_str_to_hash(self, string):
        hashmap = {}
        for char in string:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        return hashmap

    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = self.convert_str_to_hash(s)
        hashmap_t = self.convert_str_to_hash(t)
        return hashmap_s == hashmap_t

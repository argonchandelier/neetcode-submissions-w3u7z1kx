class Solution:
    def convert_str_to_hash(self, string):
        hashmap = {}
        for char in string:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        return hashmap

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        organized_anagrams = [] # answer
        ana_groups = [] # list of hashes
        for i, stri in enumerate(strs):
            striHash = self.convert_str_to_hash(stri)
            if striHash in ana_groups:
                j = ana_groups.index(striHash)
                organized_anagrams[j].append(stri)
            else:
                organized_anagrams.append([stri])
                ana_groups.append(striHash)
        print(ana_groups)
        return organized_anagrams
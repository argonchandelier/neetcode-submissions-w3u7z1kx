class Solution:
    def convert_str_to_hash(self, string):
        hashmap = {}
        for char in string:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        return hashmap

    def isAnagram(self, a, b):
        hashA = self.convert_str_to_hash(a)
        hashB = self.convert_str_to_hash(b)

        return hashA == hashB

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        organized_anagrams = [] # answer
        ana_groups = [] # list of hashes
        for i, stri in enumerate(strs):
            #group_exists = False
            striHash = self.convert_str_to_hash(stri)
            #for j, ana_group in enumerate(ana_groups):
            if striHash in ana_groups:
                j = ana_groups.index(striHash)
                organized_anagrams[j].append(stri)
                #group_exists = True
                #break
                #if not group_exists:
            else:
                organized_anagrams.append([stri])
                ana_groups.append(striHash)
        print(ana_groups)
        return organized_anagrams
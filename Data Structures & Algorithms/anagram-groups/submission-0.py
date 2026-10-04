class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i in range(len(strs)):
            string_array = list(strs[i])
            string_array.sort()
            sorted_string = ''.join(string_array)

            if sorted_string not in anagrams:
                anagrams[sorted_string] = []
            anagrams[sorted_string].append(strs[i])

        return list(anagrams.values())
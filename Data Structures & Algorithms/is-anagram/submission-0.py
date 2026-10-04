class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        turn both strings into a hashmap and then compare the values of the hashmaps
        '''

        def str_to_dict(string):
            dictionary = {}

            for letter in string:
                if letter not in dictionary:
                    dictionary[letter] = 0
                dictionary[letter] += 1
            
            return dictionary

        s_dict = str_to_dict(s)
        t_dict = str_to_dict(t)

        return s_dict == t_dict

        


        
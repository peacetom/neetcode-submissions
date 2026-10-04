class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for char in s:
            if char.isalnum() and char != ' ':
                cleaned.append(char)
        cleaned_string = ''.join(cleaned).lower()

        l, r = 0, len(cleaned_string) - 1
        while l < r:
            if cleaned_string[l] != cleaned_string[r]:
                return False
            l += 1
            r -= 1
        return True
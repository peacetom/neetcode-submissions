class Solution:
    def isValid(self, s: str) -> bool:
        
        parentheses = {
            "[" : "]",
            "(" : ")",
            "{" : "}"
        }

        stack = []

        for char in s:
            if char in parentheses:
                stack.append(char)
            else:
                if not stack:
                    return False
                popped_char = stack.pop()
                if parentheses[popped_char] != char:
                    return False

        if len(stack) > 0:
            return False

        return True

        
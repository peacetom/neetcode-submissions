class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if popped == '{' and i != '}':
                    return False         
                elif popped == '(' and i != ')':
                    return False     
                elif popped == '[' and i != ']':
                    return False
        if not stack:
            return True  
        return False              
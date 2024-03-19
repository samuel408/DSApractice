class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dictionary = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for char in s:
            if char in dictionary.values():
                stack.append(char)
            elif char in dictionary.keys():
                if not stack or stack.pop() != dictionary[char]:
                    return False
            else:
                return False
        
        return len(stack) == 0

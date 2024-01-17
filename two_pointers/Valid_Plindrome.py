import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s)  # Remove non-alphanumeric characters
        s = s.lower()  
        
        start = 0
        last = len(s)-1

        while start < last:
            if s[start]!= s[last]:
                return False
            start += 1
            last -= 1
        
        return True

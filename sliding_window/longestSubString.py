class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        test = set()
        res = 0
        left = 0         
        for i in range(len(s)):
            while s[i] in test:
                test.remove(s[left])
                left += 1
            test.add(s[i])
            res = max(res, i - left + 1)

        return res
        

        
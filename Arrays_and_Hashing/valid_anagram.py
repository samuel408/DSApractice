class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if len(s) is not len(t):
        #     return False
        #create a dictionary to store all the letters of s
        sDict = dict()
        for i in s :
            if i in sDict:
                sDict[i] += 1
            else:
                sDict[i] = 1
        #create dictionary for t
        tDict = dict()
        for i in t :
            if i in tDict:
                tDict[i] += 1
            else:
                tDict[i] = 1


        #traverse t to check if all letter in t can be found with in 
        if sDict !=  tDict :
            return False
        return True

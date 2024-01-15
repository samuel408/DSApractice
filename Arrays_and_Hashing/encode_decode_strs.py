class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    # create set to store words
    def encode(self, strs):
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res


            

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res = []
        i = 0
        
        while i < len(str):
            j = i
            while str[j] != "#":
                j+=1
                length = int(str[i:j])
                res.append(str[j+1 : j + 1 + length])
                i = j+1+length 
        return res

            



      


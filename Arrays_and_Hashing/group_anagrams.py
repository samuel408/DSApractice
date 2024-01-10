def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create a set that stores the words
        holder = collections.defaultdict(list)

        #iterate through the list of strings
        for s in strs:
            # 26 letters in the alphabetso intialize count with 26 charcters
            count = [0] * 26
            # now we need to interate over every character in each string
            for c in s:
                #for each character minus "a" is an index so count the occurences
                count[ord(c) - ord("a")] += 1

            #append the string so they are grouped together in the list 
            holder [tuple(count)].append(s)
        return holder.values()
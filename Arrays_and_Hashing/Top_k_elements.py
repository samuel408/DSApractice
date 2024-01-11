class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        regmap = defaultdict(int)
        # check nums
        for i in nums:
            if i in nums:
                regmap[i] += 1
            else:
                regmap[i] = 1
    #    sort dictionary by its key value in decensing order
        sorted_dict = OrderedDict(sorted(regmap.items(), key=lambda x: (x[1], x[0]), reverse=True))

        # grab the top K elements and put them in the solution array
        # create solution array 
        solution = []
        # top = 0
        for key in sorted_dict.keys():
            if len(solution) == k:
                break
            solution.append(key)
            i += 1
        # for key,value in regmap.items():
        #     if value > top:
        #         solution[0] = value 
        print(regmap)
        print(sorted_dict)
        return solution


       




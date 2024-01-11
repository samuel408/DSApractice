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
       # sort dictionary by its key value in decensing order
        sorted_dict = dict(sorted(regmap.items(), key=lambda x: x[1], reverse=True))

        # grab the top K elements and put them in the solution array
        # create solution array 
        solution = []
        for key in sorted_dict.keys():
            if len(solution) == k:
                break
            solution.append(key)
            i += 1

        print(regmap)
        print(sorted_dict)
        return solution


       




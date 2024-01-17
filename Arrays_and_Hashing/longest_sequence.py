class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        # sort nums 
        nums = set(nums)
        nums = sorted(nums)
        print (nums)
        longest = 1
        count = 1
        for i in range(len(nums)-1):
            print(nums[i+1])
            print (nums[i]+1)
            
            if nums[i+1] == nums[i]+1:
                count += 1
            else:
                if count > longest:
                    longest = count
                count = 1
        if count > longest:
                    longest = count
        return longest


        
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #sort the list 
        nums.sort()
        #check numbers
        for i in range(len(nums)):
            if i == len(nums) - 1:
                return False
            if( nums[i] == nums[i+1]):
                return True
        


        
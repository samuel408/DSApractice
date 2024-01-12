class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1]*len(nums)      
        for i in range(1,len(nums)):
            answer[i] = answer[i-1] * nums[i-1]

        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] = post * answer[i]
            post *= (nums[i])  


        return answer

        

            


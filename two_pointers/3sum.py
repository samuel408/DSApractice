class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and  nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1 
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
                
            

        
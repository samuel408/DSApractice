class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #create a list that is sorted
        sortedNums = sorted(nums)
        #create test variable to compare to target
        test = 0
        #create variables to store the 2sums
        one = 0
        two = 0
        
        #traverse sorted list to find numbers that add up to target numbers
        i = 0
        #create second pointer
        point = 1
        while i < len(sortedNums):
            test = sortedNums[i] + sortedNums[point]
            
            #once we find target save the two numbers and exit loop.
            if test == target:
                one = sortedNums[i]
                two = sortedNums[point]
                break

            if test > target:
                i -= 1
            else:
                i += 1  
                point += 1
        
        #once we have the numbers we can traverse the unsorted list to find the indexes
        i = 0
        solution = []
        while i < len(nums):
            if nums[i] == one or nums[i] == two:
                solution.append(i)
            i += 1
                
        return solution
            
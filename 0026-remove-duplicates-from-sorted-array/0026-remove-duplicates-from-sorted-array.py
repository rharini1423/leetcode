class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for i in range(n-1,0,-1):
            if(nums[i]==nums[i-1]):
                nums.pop(i)
        return len(nums)
        

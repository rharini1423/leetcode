class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n=len(nums)
        for i in range(n-1,-1,-1):
            if nums[i]==val:
                nums.pop(i)
        
        return(len(nums))
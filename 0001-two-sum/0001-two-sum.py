class Solution(object):
    def twoSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=list()
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]+nums[j]==target:
                    l.append(i)
                    l.append(j)
                    
        return l


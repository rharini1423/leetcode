class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l1=[]
        sum1=0
        for i in range(len(nums)):
            sum1=sum1+nums[i]
            l1.append(sum1)
        return(l1)
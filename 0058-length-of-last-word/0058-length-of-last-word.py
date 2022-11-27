class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        l=s.split(' ')
        print(l)
        length=len(l)
        lastword=len(l[length-1])
        return(lastword)
            
            
        
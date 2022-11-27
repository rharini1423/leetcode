class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=''
        for i in digits:
            s=s+str(i)
        
        res = int("".join(s))
        res=res+1
        res=str(res)
        integer=list(res)
        inte=[]
        for i in integer:
            inte.append(int(i))
            
        return(inte)
        

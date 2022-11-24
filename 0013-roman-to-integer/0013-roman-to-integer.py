class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=['I','V','X','L','C','D','M']
        l1=[1,5,10,50,100,500,1000]
        l2=[]
        val=0
        for i in s:
            l2.append(i)
        for i in range(len(l2)-1):
            first=l2[i]
            second=l2[i+1]
            pos1=l.index(first)
            pos2=l.index(second)
            if pos1<pos2:
                val=val-l1[pos1]
            else:
                val=val+l1[pos1]
        lastel=l2[-1]
        value=l1[l.index(lastel)]
        return(val+value)
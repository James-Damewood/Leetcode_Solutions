class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        hm = {}
        
        for num in A:
            if num in hm:
                return num
            else:
                hm[num] = 42
                
        return -1

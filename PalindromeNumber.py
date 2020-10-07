class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        x = str(x)
        if len(x)==1:
            return True
        
        start = 0
        end = len(x)-1
        
        while x[start] == x[end] and start<=end:
            start = start + 1
            end = end - 1
            
        if start < end:
            return False
        
        return True

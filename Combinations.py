import copy
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        out = []
        
        pointers = []
        for i in range(k):
            pointers.append(i+1)
        
        while pointers[0] <= (n)-(k-1):
            print(pointers)
            if (pointers[k-1] > n):
                #### reset pointers
                #### search for the first pointer that doesnt need to be reset
                pos = k
                found = 0
                while not found and pos > 0:
                    pos = pos - 1
                    if pointers[pos] < (n)-((k-1)-pos):
                        found = 1
                        
                pointers[pos] = pointers[pos]+1
                pos = pos + 1
                while pos <= k-1:
                    pointers[pos] = pointers[pos-1] + 1
                    pos = pos + 1
                    
                
            else:
                
                out.append(copy.deepcopy(pointers))
                pointers[k-1] = pointers[k-1]+1
            
        return out

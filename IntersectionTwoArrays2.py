class Solution(object):
    
    def get_fingerprint(self,arr):
        fp = {}
        for i in range(len(arr)):
            curr = arr[i]
            if curr in fp:
                fp[curr] = fp[curr] +1
            else:
                fp[curr] = 1
        
        
        return fp
    
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        fp_1 = self.get_fingerprint(nums1)
        fp_2 = self.get_fingerprint(nums2)
        
        ans = []
        
        for key in fp_1.keys():
            if key in fp_2:
                count = min(fp_1[key],fp_2[key])
                for j in range(count):
                    ans.append(key)
        
        
        
        return ans

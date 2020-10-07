import copy
class Solution(object):
    
    def get_n(self,image,r,c):
        n = []
        x = len(image)
        y = len(image[0])
        if (r > 0):
            curr = (r-1,c)
            n.append(curr)
        if (r < x-1):
            curr = (r+1,c)
            n.append(curr)
        if (c>0):
            curr = (r,c-1)
            n.append(curr)
        if (c<y-1):
            curr = (r,c+1)
            n.append(curr)
        return n
    
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if len(image) == 0:
            return image
        
        const = copy.deepcopy(image[sr][sc])
        
        is_visited = {}
        
        queue = collections.deque()
        is_visited[(sr,sc)] = 1
        queue.appendleft((sr,sc))
        while queue:
            r,c = queue.pop()
            if (image[r][c] == const):
                image[r][c] = newColor
                n = self.get_n(image,r,c)
                for n_index in range(len(n)):
                    n_r,n_c = n[n_index]
                    if ((n_r,n_c) not in is_visited):
                        is_visited[(n_r,n_c)]=1
                        queue.appendleft((n_r,n_c))
        
        return image

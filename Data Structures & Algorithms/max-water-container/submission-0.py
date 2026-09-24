class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxa = 0
        while(i < j):
            idx = min(i, j, key=lambda x: heights[x])
            area = heights[idx] * (j - i)
            maxa = max(maxa, area)
            if(idx == i):
                i+=1
            else:
                j-=1
        return maxa



            

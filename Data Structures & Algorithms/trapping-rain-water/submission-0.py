class Solution:
    def trap(self, height: List[int]) -> int:
        maxa = 0
        prefix = []
        suffix = []
        for i in range(len(height)):
            maxa = (max(maxa, height[i]))
            prefix.append(maxa)
        maxa = 0
        for i in range(len(height)):
            maxa = (max(maxa, height[len(height)-1-i]))
            suffix.append(maxa)
        sum = 0
        for i in range(len(height)):
            sum += min(prefix[i], suffix[len(height)-1-i]) - height[i]
        
        return sum
        
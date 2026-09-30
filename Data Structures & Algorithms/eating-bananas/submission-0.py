class Solution:
    def check(self, piles, k, h):
        s=0
        for x in piles:
            if(x%k==0):
                s+=x//k
            else:
                s+=x//k+1
        return s <= h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while(left<=right):
            mid = (left+right)//2
            if(self.check(piles, mid, h)):
                right = mid - 1
            else:
                left = mid + 1
        return left
                

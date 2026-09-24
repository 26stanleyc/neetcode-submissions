class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        sols = set()
        for k in range(len(nums) - 2):
            i, j = k+1, len(nums) - 1
            target = -nums[k]
            while(i < j):
                sum = nums[i] + nums[j]
                if(sum == target):
                    sols.add((nums[i], nums[j], nums[k]))
                    i+=1
                    j-=1
                elif(sum < target):
                    i+=1
                else:
                    j-=1
        return [list(t) for t in sols]
                



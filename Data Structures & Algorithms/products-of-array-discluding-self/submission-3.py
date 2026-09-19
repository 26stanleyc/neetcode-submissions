class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        a=1
        for i in range(len(nums)-1):
            a*=nums[i]
            prefix.append(a)
        a=1
        for i in range(len(nums)-1, -1, -1):
            a*=nums[i]
            suffix.append(a)
        return [prefix[i]*suffix[len(nums)-i-1] for i in range(len(nums))]

        
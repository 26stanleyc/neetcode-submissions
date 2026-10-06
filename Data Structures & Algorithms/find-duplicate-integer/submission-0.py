class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = {}
        for i in range(len(nums)):
            if(nums[i] in visited):
                return nums[i]
            visited[nums[i]] = 1
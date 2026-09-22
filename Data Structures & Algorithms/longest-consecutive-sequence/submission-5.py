class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        s = sorted(nums)
        max_length = 0
        curr_length = 1
        for i in range(len(s)-1):
            if(s[i] == s[i+1]):
                continue
            elif(s[i] + 1 == s[i+1]):
                curr_length+=1
            else:
                max_length = max(curr_length, max_length)
                curr_length = 1
        max_length = max(curr_length, max_length)
        return max_length
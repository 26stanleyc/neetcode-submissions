class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if(nums[i] not in dict):
                dict[nums[i]]=1
            else:
                dict[nums[i]]+=1
        sorted_d = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
        return [key for key, _ in sorted_d[:k]]
            
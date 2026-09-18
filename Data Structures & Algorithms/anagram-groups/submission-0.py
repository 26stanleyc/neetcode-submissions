class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            text = "".join(sorted(s))
            if text not in groups:
                groups[text] = []
            groups[text].append(s)
        return list(groups.values())
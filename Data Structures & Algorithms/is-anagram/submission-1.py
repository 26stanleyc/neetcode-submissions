class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visited = {}
        for i in s:
            if i not in visited:
                visited[i] = 1
            else:
                visited[i] += 1
        tvisited = {}
        for i in t:
            if i not in tvisited:
                tvisited[i] = 1
            else:
                tvisited[i] += 1
        return visited == tvisited
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        news = ""
        for x in s:
            if(x.isalnum()):
                news += x
        i, j = 0, len(news) - 1
        while(i < j):
            if(news[i] != news[j]):
                return False
            i+=1
            j-=1
        return True

        
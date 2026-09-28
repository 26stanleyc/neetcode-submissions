class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        missing = len(t)          # how many chars of t are still unmatched
        left = 0
        best_start, best_len = 0, float('inf')

        for right, ch in enumerate(s):
            # expand: take in s[right]
            if need.get(ch, 0) > 0:
                missing -= 1
            need[ch] = need.get(ch, 0) - 1

            # window is valid: shrink from the left as far as possible
            while missing == 0:
                if right - left + 1 < best_len:
                    best_start, best_len = left, right - left + 1

                out = s[left]
                need[out] += 1
                if need[out] > 0:     # we just removed a char we needed
                    missing += 1
                left += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]
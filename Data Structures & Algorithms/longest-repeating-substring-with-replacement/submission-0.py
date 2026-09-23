class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        count = defaultdict(int)
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1 
            window = right - left + 1
            if window - max(count.values()) <= k:
                res = max(res, window)
            else:
                count[s[left]] -= 1
                left += 1


        return res

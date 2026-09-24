class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0

        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1) - 1])

        for right in range(len(s1) - 1,len(s2)):
            window_count[s2[right]] += 1
            if s1_count == window_count:
                return True
            else:
                window_count[s2[left]] -= 1
                left += 1


        return False
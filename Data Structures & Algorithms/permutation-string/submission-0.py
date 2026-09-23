class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0

        for right in range((len(s1) - 1) , len(s2)):
            if Counter(s1) == Counter(s2[left:right+1]):
                return True
            left += 1

        return False
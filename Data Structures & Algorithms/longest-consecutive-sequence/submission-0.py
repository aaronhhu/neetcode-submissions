class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maximum = 1
        s = set(nums)
        
        for i in s:
            if i - 1 not in s:
                output = 1
                while i + output in s:
                    output += 1
                if output > maximum:
                    maximum = output

        return maximum
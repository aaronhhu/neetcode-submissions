class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ints = {}

        for index, value in enumerate(nums):
            difference = target - value

            if difference in ints and index != ints[difference]:
                return [ints[difference], index]

            ints[value] = index
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total = 0

        leftH = height[0]
        rightH = height[right]

        while left < right:
            if leftH < rightH:
                left += 1
                if height[left] > leftH:
                    leftH = height[left]
                else:
                    total += (leftH - height[left])

            else:
                right -= 1
                if height[right] > rightH:
                    rightH = height[right]
                else:
                    total += (rightH - height[right])


        return total
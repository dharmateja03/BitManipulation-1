# TimeComplexity:O(n)
# SpaceComplexity:O(1)
# Appraoch:if we use xor on all nums in list equal number will cancel out

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            a=a^i
        return a
        

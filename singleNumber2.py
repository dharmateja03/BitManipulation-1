# TimeComplexity:O(n)
# SpaceComplexity:O(1)


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        similar to single number problem , use xor 
        but you will get xor fo two missing numbers how to get two number out of those numbers
        find least siginifiact digit useing 2s complement with this you can find digit which is not same 
        in both numbers

        """

        xor=0
        for i in nums:
            xor =xor^i
        #find 2'complemnt
        
        lsb= xor & (-1*xor)
        ans1=0
        for i in nums:
            if i&lsb!=0:
              
                ans1=ans1^i
        return [ans1,ans1^xor]


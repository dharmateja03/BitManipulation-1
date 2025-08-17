TimeComplexity:O(logn )
SpaceCompelxity:O(1)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        yeah , brute force would be multiply untill you get >= dividend ,  be carful about both being negative
        logn base 2 approch woudl be  
         find number of shifts that will number take and subtract it 
         like lets say 
          34/4 
           4*2=8
           8*2=16
           16*2= 34
           34*2=68 -->stop 
           you need 1<<4 ==8

           ---
           25/3
           3*2=6
           6*2=12
           12*2=24
           24*2=48 -->stop
            4 steps
        
        ----
        25/4
        4*2=8
        8*2=16 untill now ans =  3 steps so "4"
        16*2=32-- stop
        but 25-16=9 you still have 9 to deal with
        follow same 9/4
        4*2=8
        8*2=16 --stop
        need 2 steps so 2
        4+2=6


        """
        #edge case
        if dividend==-2147483648 and divisor==-1:return -1*dividend-1 
        ans=0
        odivisor=divisor
        odividend=dividend
        if divisor<0:divisor=-1*divisor
        if odividend<0: dividend=-1*odividend

        while(dividend>=divisor):
            # print(dividend,"dive")
            steps=0
            k=divisor
            while(dividend>=k):
                k=k*2
                steps+=1
                # print(k,"kdive")
            
            steps-=1
            ans+= (1<<steps)
            dividend-=(divisor<<steps)
        if (odividend>0 and odivisor>0) or (odividend<0 and odivisor<0):
            return ans
        return -1*ans

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=float("inf")
        maxpr=0

        for p in prices:

            if p <= minp:
                minp=p
            elif p - minp > maxpr:
                maxpr=p-minp

        return maxpr
        
        
        
           

           




 
        
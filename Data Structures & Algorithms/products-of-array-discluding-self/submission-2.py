class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        
        # 1. Count zeros and find the product of non-zero numbers
        for i in nums:
            if i == 0:
                zero_count += 1  # Fixed typo (o instead of 0)
            else:
                prod *= i

        # 2. Quick return if there are multiple zeros
        if zero_count > 1:
            return [0] * len(nums)

        # 3. Calculate results using direct index assignment
        res = [0] * len(nums)
        for idx, i in enumerate(nums):
            if zero_count == 1:
                res[idx] = prod if i == 0 else 0
            else:
                res[idx] = prod // i  # Direct assignment prevents list doubling
                
        return res

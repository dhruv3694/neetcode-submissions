class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1

        sorted_items = sorted(frequency_map.items(), key=lambda item: item[1], reverse=True)
        top_k_keys = [item[0] for item in sorted_items[:k]]
        
        return top_k_keys
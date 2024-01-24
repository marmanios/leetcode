class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []

        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        
        top_k_counts = list(hash_map.values())
        top_k_counts.sort(reverse=True)
        while True:
            for num in hash_map:
                if hash_map[num] == top_k_counts[0]:
                    result.append(num)
                    top_k_counts.remove(hash_map[num])
                    hash_map[num] = 0

                    if len(result) == k: return result


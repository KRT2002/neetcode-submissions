class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num]+=1
        
        sorted_list = sorted(hashmap.items(), key=lambda k:k[1], reverse=True)
        sorted_hashmap = {k:v for k, v in sorted_list}
        output = list(sorted_hashmap.keys())[:k]
        return output
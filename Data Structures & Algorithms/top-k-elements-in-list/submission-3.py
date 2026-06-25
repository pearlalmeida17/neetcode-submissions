class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash = {}

        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1

        sorted_for_k = dict(sorted(hash.items(), key =lambda x: x[1], reverse = True))
        list_keys = list(sorted_for_k.keys())

        keys = []
        for j in range(k):
            keys.append(list_keys[j])
            
        return keys



        
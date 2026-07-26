class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        result = []
        for i in nums:
            if i not in a.keys():
                a[i] = nums.count(i)
        print(a)
        sorted_items = sorted(a.items(), key=lambda x: x[1], reverse=True)
        print(sorted_items)
        for key, value in sorted_items[:k]:
            result.append(key)
        return(result)
        






class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        result = []
        for x in strs:
            a[tuple(sorted(x))].append(x)
        print(a)
        for i in a.values():
            result.append(i)
        return(result)



                
        
        
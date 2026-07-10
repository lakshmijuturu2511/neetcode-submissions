class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        res=[]
        for word in strs:
            sorted_word=sorted(word)
            sorted_word="".join(sorted_word)
            if sorted_word not in d:
                d[sorted_word]=[]
            d[sorted_word].append(word)
        for key,value in d.items():
            res.append(value)
        return res
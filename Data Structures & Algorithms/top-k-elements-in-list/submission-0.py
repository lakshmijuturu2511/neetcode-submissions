class Solution:
    
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        mp = Counter(nums)

    # Store the elements of 'mp' in the list 'freq'
        freq = list(mp.items())

    # Sort the list 'freq' on the basis of the
    # 'compare' function
        freq.sort(key=lambda x: (x[1], x[0]), reverse=True)
    
        res = []
    
    # Extract and store the top k frequent elements
        for i in range(k):
            res.append(freq[i][0])
        
        return res
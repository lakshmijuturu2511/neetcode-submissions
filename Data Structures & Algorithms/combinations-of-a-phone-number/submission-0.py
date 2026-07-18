class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        res = [""]

        for ch in digits:
            temp = []
            num = int(ch)

            for word in res:
                for letter in d[num]:
                    temp.append(word + letter)

            res = temp

        return res
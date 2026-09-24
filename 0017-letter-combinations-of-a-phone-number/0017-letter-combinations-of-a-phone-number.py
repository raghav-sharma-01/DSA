class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not  digits:
            return []
        phone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        result = []

        def bracktrack(index, current):
            if index == len(digits):
                result.append(current)
                return
            letters = phone[digits[index]]
            for ch in letters:
                bracktrack(index+1, current+ch)
        bracktrack(0, "")
        return result                
        
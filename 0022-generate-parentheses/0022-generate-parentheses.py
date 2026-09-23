class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def para(s, open, close):
            if open == n and close == n:
                ans.append(s)
                return
            if open < n:
                para(s+'(',open+1,close)
            if close < open:
                para(s+')',open,close+1)
        para("",0,0)
        return ans                
        
        
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # count of the opening parentehsis = count of the clsoing parenthesis = n
        # add an opening parenthesis when it is < n
        # add a closing parenthesis when count of open > closed count

        par = []
        res = []

        def backtracking(opened, closed):
            if opened == closed == n:
                res.append("".join(par))
                return
            if opened < n:
                par.append("(")
                backtracking(opened + 1, closed)
                par.pop()
            if closed < opened:
                par.append(")")
                backtracking(opened, closed + 1)
                par.pop()
        
        backtracking(0,0)
        return res


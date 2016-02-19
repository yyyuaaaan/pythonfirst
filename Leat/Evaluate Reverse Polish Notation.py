"""__author__ = 'anyu'
Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        if tokens is None: return None
        if len(tokens) is 1: return int(tokens[0])
        else:
            for x in tokens: #
                if x  not in ["+" , "-" , "*" , "/"]:
                    stack.append(x)
                else:
                    t2 = int(stack.pop()) # pay attention to order of t1 t2
                    t1 = int(stack.pop())
                    result = 0
                    if x is "+": result = t1+t2
                    if x is "-": result = t1 - t2
                    if x is "*": result = t1*t2
                    if x is "/":
                        if t2 is 0: print "zero devision"; return
                        result = t1/t2 # integer devision
                    stack.append(result)
            return stack.pop()

s = Solution()
# python 6/(-132) == -1
print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
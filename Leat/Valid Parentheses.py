"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') stk.push(c);
            else {
                if (stk.empty()) return false;
                else if (c == ')' && stk.top() == 'c') stk.pop();
                else if (c == ']' && stk.top() == '[') stk.pop();
                else if (c == '{' && stk.top() == '}') stk.pop();
                else return false;
            }
        }
        return (stk.empty());
    }
};
stack

"""
def isValid(s):
    if len(s) is 0: return True
    stack = []
    for char in s:
        if char in ['(','{','[']:
            stack.append(char)
        else:
            if not stack: return False
            elif char is ')' and stack.pop() is '(': continue
            elif char is '}' and stack.pop() is '{': continue
            elif char is ']' and stack.pop() is '[': continue
            else: return False

    return stack ==[]

print isValid("[]")
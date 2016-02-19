"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

class Solution {
public:
    vector<int> plusOne(vector<int> &digits) {
        int carry = 1, N = digits.size();
        for (int i = N-1; i >= 0 && carry; --i)
        {
            int sum = carry + digits[i];
            carry = sum / 10;
            digits[i] = sum % 10;
        }
        if (carry == 1)
            digits.insert(digits.begin(), 1);
        return digits;
    }
};
"""
def plusone(digitlist):
    carry = 1
    for i in reversed(range(len(digitlist))):
        sum = carry + digitlist[i]
        carry = sum/10
        if carry is 0: break
        digitlist[i] = sum % 10
    if carry is 1:
        digitlist = [1]+digitlist
    return digitlist

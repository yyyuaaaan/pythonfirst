"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

 Solution: dfs...
 */

class Solution {
public:
    vector<vector<int>> res;

    vector<vector<int>> permute(vector<int> &num) {
        res.clear();
        vector<bool> avail(num.size(), true);
        vector<int> pum;
        permuteRe(num, avail, pum);
        return res;
    }

    void permuteRe(const vector<int> &num, vector<bool> &avail, vector<int> &pum)
    {
        if (pum.size() == num.size())
        {
            res.push_back(pum);
            return;
        }
        for (int i = 0; i < num.size(); ++i)
        {
            if (avail[i])
            {
                avail[i] = false;
                pum.push_back(num[i]);
                permuteRe(num, avail, pum);
                pum.pop_back();
                avail[i] = true;
            }
        }
    }
};
"""
def permutations(s):
    if not s: return []
    if len(s) is 1: return s

    last =[s[0]]
    for i in range(len(s)-1):
        nextl = []
        for x in s[1:]:
            for permu in last:
                for i in range(len(permu)):
                    nextl+= permu[:i]+[x]+permu[i:]
        last = nextl
    return nextl



print permutations([1,2,3])
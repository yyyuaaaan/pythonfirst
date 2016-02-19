"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
 This solution is from Peking2 (http://blog.sina.com.cn/s/blog_b9285de20101iqar.html).
           This solution is much easier to understand.

class Solution {
public:
    int longestConsecutive(vector<int> &num) {
        unordered_set<int> s;
        int res = 0;
        for (int i = 0; i < num.size(); ++i)
            s.insert(num[i]);
        for (int i = 0; i < num.size() && !s.empty(); ++i)
        {
            int upper = num[i], lower = num[i];
            while (s.find(upper+1) != s.end())
                s.erase(++upper);
            while (s.find(lower-1) != s.end())
                s.erase(--lower);
            res = max(res, upper - lower + 1);
        }
        return res;
    }
};
"""

def longestConsecutive(num):
    """
    this sol has problem,use list as a hashtable
    """
    s= set(num) # hashtable

    res = 0
    size = len(s)
    i =0

    while i in range(size-1) and len(s) is not 0:
        upper = num[i]
        lower = num[i]
        while upper+1 in s:
            s.remove(upper)
            upper+=1
        while lower+1 in s:
            s.remove(lower)
            lower+=1
        res = max(res,upper-lower+1)
    return res








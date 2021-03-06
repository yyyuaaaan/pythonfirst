"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

I like brute force better than dfs
dfs is a misnomer here, it is actually recursion


For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> res;
        string ip;
        restoreIpAddressRe(s, res, ip, 0, 0);
        return res;
    }

    void restoreIpAddressRe(string &s, vector<string> &res, string &ip, int deep, int start)
    {
        if (deep == 4 && start == s.size())
            res.push_back(ip);
        if (deep == 4) return;

        int num = 0, origSize = ip.size();
        if (origSize != 0) ip.push_back('.');
        for (int i = start; i < s.size(); ++i)
        {
            num = num * 10 + s[i] - '0';
            if (num > 255) break;
            ip.push_back(s[i]);
            restoreIpAddressRe(s, res, ip, deep + 1, i + 1);
            if (num == 0) break;
        }
        ip.resize(origSize);
    }
};
"""
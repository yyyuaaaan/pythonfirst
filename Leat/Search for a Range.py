"""
class Solution {
public:
    vector<int> searchRange(int A[], int n, int target) {
        vector<int> res(2, -1);
        int lower = getLowerBound(A, n, target);
        int upper = getUpperBound(A, n, target);
        if (lower <= upper)
        {
            res[0] = lower;
            res[1] = upper;
        }
        return res;
    }

    int getLowerBound(int A[], int n, int target)
    {
        int l = 0, u = n-1;
        while (l <= u)
        {
            int mid = (l + u) / 2;
            if (A[mid] < target)
                l = mid + 1;
            else
                u = mid - 1;
        }
        return l;
    }

    int getUpperBound(int A[], int n, int target)
    {
        int l = 0, u = n-1;
        while (l <= u)
        {
            int mid = (l + u) / 2;
            if (A[mid] <= target)
                l = mid + 1;
            else
                u = mid - 1;
        }
        return u;
    }
};
"""
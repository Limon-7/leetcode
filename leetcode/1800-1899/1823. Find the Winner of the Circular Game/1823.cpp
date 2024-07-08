class Solution
{
    int helper(int n, int k)
    {
        int res = 0;

        if (n == 1)
            return 1;

        res = (helper(n - 1, k) + k) % n;

        return res == 0 ? n : res;
    }

public:
    int findTheWinner(int n, int k) { return helper(n, k); }
};

// TC: O(N) SC:O(N)
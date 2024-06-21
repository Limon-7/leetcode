class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0)
            return 1;
        if (x == 0)
            return 0;

        double res = 1;
        long long nn = n;
        nn = nn > 0 ? nn : -1 * nn;
        while (nn) {
            if (nn & 1) {
                res = res * x;
                nn = nn - 1;
            } else {
                x = x * x;
                nn = nn >> 1;
            }
        }
        return n > 0 ? res : 1.0 / res;
    }
};
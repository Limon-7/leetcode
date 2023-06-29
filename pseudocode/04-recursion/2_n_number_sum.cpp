#include <iostream>
using namespace std;

int sum(int n)
{
    int sum = 0;
    for (int i = 1; i <= n; ++i)
    {
        sum += i;
    }
    return sum;
}

int sum_recursive(int n, int sum)
{
    if(n==0) return sum;

    return sum_recursive(n-1, sum+n);
}

int sum_recursive2(int n)
{
    if(n==0) return 0;

    return n + sum_recursive2(n-1);
}

int main()
{
    int n = 100;
    cout << "Sum of 1 to 100 = " << sum(100) << endl;
    cout << "Sum of 1 to 100 = " << (100*101)/2 << endl;// n(n+1)/2
    cout << "Sum of 1 to 100 = " << sum_recursive(100,0) << endl;

    cout << "Sum of 1 to 100 = " << sum_recursive2(100) << endl;

    return 0;
}
/**
 * Time complexity: O(N)
 * Space Complexity: O(N)
*/
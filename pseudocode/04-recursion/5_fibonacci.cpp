#include <iostream>
#include <algorithm>
#include <ctype.h>

using namespace std;

void naive(int n)
{
    if (n == 0)
        cout << 0 << " ";
    else if (n == 1)
        cout << 0 << " " << 1 << endl;
    else
    {
        int fib[n + 1];
        fib[0] = 0;
        fib[1] = 1;
        for (int i = 2; i <= n; i++)
        {
            fib[i] = i;
        }
        for (int i = 0; i <= n; ++i)
        {
            cout << fib[i] << " ";
        }
    }
    /**
     * Time complexity: O(N)+O(N)
     * Space Complexity: O(N)
     */
}

void optimized(int n)
{
    if (n == 0)
        cout << 0 << " ";
    else if (n == 1)
        cout << 0 << " " << 1 << endl;
    else
    {
        int p1 = 0;
        int p2 = 1;
        cout << p1 << " " << p2 << " ";
        int current;
        for (int i = 2; i <= n; i++)
        {
            current = p1 + p2;
            p1 = p2;
            p2 = current;
            cout << current << " ";
        }
    }
    /**
     * Time complexity: O(N)
     * Space Complexity: O(1)
     */
}

int fibonacci(int N)
{
    if (N <= 1)
    {
        return N;
    }
    int last = fibonacci(N - 1);
    int slast = fibonacci(N - 2);

    return last + slast;
    /**
     * Time Complexity: O(2^N) { This problem involves two function calls for each iteration which further expands to 4 function calls and so on which makes worst-case time complexity to be exponential in nature }.
     * Space Complexity: O(N)
    */
}
int main()
{
    int n = 5;
    naive(n);
    optimized(n);
    cout << "\n"
         << fibonacci(2);
    return 0;
}
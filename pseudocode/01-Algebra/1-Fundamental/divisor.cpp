#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int n = 20;
    int d = 0;
    for (int i = 1; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            d += 1;
            cout << i << " ";
            if (i != n / i)
            {
                cout << n / i << " ";
                d += 1;
            }
        }
    }
    cout << "divisor:" << d << endl;
    return 0;
}
/**
 * Time Complexity: O(sqrt(n))
 * Space Complexity: O(1)
 */
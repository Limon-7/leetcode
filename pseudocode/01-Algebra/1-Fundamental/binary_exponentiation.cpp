#include <iostream>
using namespace std;

int binary_exponentiation(int base, int exponent)
{
    int result = 1;
    while (exponent > 0)
    {
        // if (exponent % 2 == 1)
        if (exponent & 1)
            result *= base;
        base *= base;
        exponent >>=1;
    }

    return result;
}
int main()
{
    cout<<binary_exponentiation(3,5)<<endl;

    return 0;
}
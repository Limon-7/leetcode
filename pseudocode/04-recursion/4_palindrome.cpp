#include <iostream>
#include <algorithm>
#include <ctype.h>

using namespace std;

void traverse(int arr[], int s)
{
    cout << "Traverse array:\n";
    for (int i = 0; i < s; ++i)
    {
        cout << arr[i] << " ";
    }
    cout << "\nEnding Traverse" << endl;
}
bool checkPalindrome_recursive(string &str, int s)
{
    if (s >= str.length() / 2)
        return true;

    if (str[s] != str[str.length() - s - 1])
        return false;

    return checkPalindrome_recursive(str, s + 1);
}

bool checkPalindrome(string str, int l)
{
    string temp = str;
    int p1 = 0;
    int p2 = l - 1;
    while (p1 < p2)
    {
        // swap(str[p1++], str[p2--]);
        if (!isalnum(str[p1])) // Checks whether c is either a decimal digit or an uppercase or lowercase letter. 
            ++p1;
        else if (!isalnum(str[p2]))
            --p2;
        else if (tolower(str[p1]) != tolower(str[p2]))
            return false;
        else
        {
            ++p1;
            --p2;
        }
    }
    return true;

    // cout << temp << "  " << str << endl;
}
int main()
{
    string str = "ABCDCBA";
    int s = str.length();
    cout << checkPalindrome(str, s) << endl;
    cout << checkPalindrome_recursive(str, 0) << endl;
    return 0;
}
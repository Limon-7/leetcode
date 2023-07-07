#include <iostream>
#include <algorithm>

using namespace std;

int bruteForce(int arr[], int n)
{
    sort(arr, arr + n);
    return arr[n - 1];
    /**
     * Time complexity: O(NlogN)
     * Space Complexity: O(1)
     */
}
int optimal(int arr[], int n)
{
    int largest = arr[0];
    for (int i = 1; i < n; i++)
    {
        if (arr[i] >= largest)
            largest = arr[i];
    }
    return largest;
    /**
     * Time complexity: O(N)
     * Space Complexity: O(1)
     */
}

int main()
{
    int arr[] = {1, 5, 8, 9, 6, 7, 3, 4, 2, 100};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "bruteForce: " << bruteForce(arr, n) << endl;
    cout << "optimal: " << optimal(arr, n) << endl;
    return 0;
}
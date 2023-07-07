#include <iostream>
#include <algorithm>

using namespace std;

void bruteForce(int arr[], int n)
{
    if (n < 2)
    {
        cout << -1;
    }
    sort(arr, arr + n); // O(NLog(N))

    int secondLargest = arr[n - 2];
    int secondSmallest = arr[1];

    for (int i = n - 2; i >= 0; ++i) // O(N)
    {
        if (arr[i] < arr[n - 1])
        {
            secondLargest = arr[i];
            break;
        }
    }

    for (int i = 0; i < n - 2; i++) // O(N)
    {
        if (arr[i] < arr[i + 1])
        {
            secondSmallest = arr[i + 1];
            break;
        }
    }
    cout << secondSmallest << " " << secondLargest << "\n";
    /**
     * Time complexity: O(NlogN)+ O(N)+ 0(N) == O(NlogN)+ O(2N)
     * Space Complexity: O(1)
     */
}

void better(int arr[], int n)
{
    int small = INT_MAX;
    int secondSmall = INT_MAX;
    int large = INT_MIN;
    int secondLarge = INT_MIN;

    for (int i = 0; i < n; ++i)
    {
        // if (arr[i] < small)
        // {
        //     small = arr[i];
        // }

        // if (arr[i] > large)
        // {
        //     large = arr[i];
        // }
        large = max(large, arr[i]);
        small = min(small, arr[i]);

    } // O(N)

    // cout << small << " " << large << endl;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] != small && arr[i] < secondSmall)
            secondSmall = arr[i];
        if (arr[i] != large && arr[i] > secondLarge)
            secondLarge = arr[i];
    } // O(N)
    cout << secondSmall << " " << secondLarge << endl;
}
// TC: O(N) We do two linear traversals in our array
// SC: O(1)

void optimal(int arr[], int n)
{
    int small = INT_MAX;
    int secondSmall = INT_MAX;
    int large = INT_MIN;
    int secondLarge = INT_MIN;

    for (int i = 0; i < n; ++i)
    {
        if (arr[i] < small)
        {
            secondSmall = small;
            small = arr[i];
        }
        if (arr[i] < secondSmall && arr[i] != small)
        {
            secondSmall = arr[i];
        }

        if (arr[i] > large)
        {
            secondLarge = large;
            large = arr[i];
        }
        if (arr[i] > secondLarge && arr[i] != large)
        {
            secondLarge = arr[i];
        }
    }
    cout << secondSmall << " " << secondLarge << endl;
    /**
     * Time complexity: O(N)
     * Space Complexity: O(1)
     */
}

int main()
{
    int arr[] = {1, 5, 8, 9, 6, 7, 3, 4, 2, 100};
    int n = sizeof(arr) / sizeof(arr[0]);

    bruteForce(arr, n);
    better(arr, n);
    optimal(arr, n);

    return 0;
}
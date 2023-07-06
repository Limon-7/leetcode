#include <bits/stdc++.h>

using namespace std;

void countFrequency(int arr[], int n)
{    
    vector<bool> visited(n, false);

    for (int i = 0; i < n; i++)
    {
        if (visited[i]== true)
            continue;
        
        int count = 1;
        for (int j = i + 1; j < n; j++)
        {
            if (arr[i] == arr[j])
            {
                count += 1;
                visited[j] = true;
            }
        }
        cout << arr[i] << " " << count << endl;
    }
    /**
     * Time complexity: O(N*N)
     * Space Complexity: O(N)
    */
}
int main()
{

    #ifndef ONLINE_JUDGE
    freopen("../input.txt","r",stdin);
    freopen("../output.txt","w",stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int t;
    // cout << "enter test case: ";
    cin >> t;
    while (t--)
    {
        int n, p;
        // cout << "enter array size: ";
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        countFrequency(arr, n);
    }
    return 0;
}
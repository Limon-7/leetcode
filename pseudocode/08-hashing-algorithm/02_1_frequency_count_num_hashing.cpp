#include <bits/stdc++.h>

using namespace std;

int main()
{

    #ifndef ONLINE_JUDGE
    freopen("../input.txt","r",stdin);
    freopen("../output.txt","w",stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }

        int q;
        cin>>q;
        vector<int> hash(n+1, 0);

        for(int i=0; i<n; i++){
            hash[arr[i]]++;
        }

        while(q--){
            int num;
            cin>>num;
            cout<<num<<" "<<hash[num]<<"\n";
        }
    }
    return 0;
}
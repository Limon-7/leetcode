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
        string s;
        cin>>s;

        int q;
        cin>>q;
        vector<int> hash(26, 0);//for lowercase/uppercase. if call cases 256

        for(int i=0; i<s.size(); i++){
            hash[s[i]-'a']++;
        }

        while(q--){
            char  ch;
            cin>>ch;
            cout<<ch<<" "<<hash[ch-'a']<<"\n";
        }
    }
    return 0;
}
#include<iostream>
#include<math.h>
using namespace std;


int main(){
    int n= 370;
    int l = to_string(n).length();
    int sum=0;
    int temp =n;

    while(n>0){
        int d= n%10;
        sum += pow(d,l);
        n/=10;
    }
    if(sum==temp) cout<<1<<endl;
    else cout<<0;
    // cout<<sum<<endl;

    return 0;
}
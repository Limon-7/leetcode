#include<iostream>
using namespace std;

unsigned long long int factorial(int n){
    int fact = 1;
    for(int i=i;i<=n;++i){
        fact*=i;
    }
    return fact;
}
unsigned long long int factorial_recusive(int n){
    if(n==1) return 1;
    return n*factorial_recusive(n-1);
}
unsigned long long int factorial_recusive2(int n,int fact){
    if(n==1) return fact;
    return factorial_recusive2(n-1, fact*n);
}

int main(){
    cout<<"Iterative: factorial of 7 = "<<factorial(5)<<endl;
    cout<<"Recursive: factorial of 7 = "<<factorial_recusive(5)<<endl;
    cout<<"Recursive-2: factorial of 7 = "<<factorial_recusive(5)<<endl;

    return 0;
}
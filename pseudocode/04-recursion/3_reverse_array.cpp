#include <iostream>
#include<algorithm>

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
void reverse_iterative(int arr[], int s){
    int temp[s];

    for(int i= 0 ; i<s; i++){
        temp[s-i-1] = arr[i]; 
    }
    traverse(temp,s);
    /**
     * Time complexity: O(N)
     * Space Complexity: O(N)
    */
}

void reverse_pointer(int arr[], int s){
    int p1=0;
    int p2=s-1;
    while(p1<p2){
        swap(arr[p1++], arr[p2--]);
        // ++p1; --p2;
    }
    traverse(arr,s);
    /**
     * Time complexity: O(N)
     * Space Complexity: O(1)
    */
}
void reverse_pointer_recursion(int arr[], int s, int e){
    if(s<e){
        swap(arr[s], arr[e]);
        reverse_pointer_recursion(arr, s+1, e-1);
    }
   
    /**
     * Time complexity: O(N)
     * Space Complexity: O(1)
    */
}
void reverse_builtin(int arr[], int s){
    reverse(arr, arr+s);
    traverse(arr,s);
}

int main()
{
    int arr[] = {5, 4, 3, 2, 1};
    int s = sizeof(arr) / sizeof(arr[0]);
    traverse(arr, s);
    // reverse_iterative(arr, s);
    // reverse_pointer_recursion(arr, 0, s-1);
    // traverse(arr,s);
    // reverse_pointer(arr,s);
    reverse_builtin(arr,s);
    return 0;
}
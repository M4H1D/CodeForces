#include <bits/stdc++.h>
using namespace std;
int main(){
    int arr[3],t;
    cin>>t;
    while(t--){
        cin>>arr[0]>>arr[1]>>arr[2];
        sort(arr,arr+3);
        cout<<arr[1]<<endl;
    }
    return 0;
}
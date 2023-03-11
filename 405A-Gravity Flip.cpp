#include<bits/stdc++.h>
#include<cmath>
#include<algorithm>
using namespace std;
int main(){
    int n;cin>>n;
    int array[n];
    for (int i=0;i<n;++i){cin>>array[i];}
    int size=sizeof(array)/sizeof(array[0]);
    sort(array,array+size);
    for (int m=0;m<n;++m){cout<<array[m]<<" ";}

    return 0;
}
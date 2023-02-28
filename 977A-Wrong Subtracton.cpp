#include <iostream>
using namespace std;
int main(){
    int t,n;
    cin>>n>>t;
    while(t--){
        if(n%10==0){n=n/10;}
        else{n-=1;}
    }cout<<n;
    return 0;
}
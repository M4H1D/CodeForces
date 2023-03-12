#include<bits/stdc++.h>
#include<cmath>
#include<algorithm>
using namespace std;
int main(){
    int t,x,y;cin>>t;
    while(t--){
        cin>>x>>y;
        int x1=abs(x),y1=abs(y);
        if (x1==y1){cout<<x1+y1<<endl;}
        else{
            int z=max(x1,y1);
            cout<<2*z-1<<endl;
        }

    }

    return 0;
}
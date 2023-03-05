#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;cin>>t;
    while(t--){
        int x,y;cin>>x>>y;
        if(x<y){cout<<y-x<<endl;}
        else if(x>=y){
            if(x%y==0){cout<<0<<endl;}
            else{int z=(x/y)+1;
                cout<<z*y-x<<endl;}
        }
    }
    return 0;
}
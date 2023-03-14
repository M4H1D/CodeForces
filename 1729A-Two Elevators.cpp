#include<bits/stdc++.h>
#include<cmath>
#include<algorithm>
using namespace std;
int main(){
    int a,b,c,t;cin>>t;
    while(t--){
        cin>>a>>b>>c;
    int x=abs(a-1),y=abs(b-c)+abs(c-1);
    if (x<y){cout<<1<<endl;}
    else if(x>y){cout<<2<<endl;}
    else{cout<<3<<endl;}}
    return 0;
}
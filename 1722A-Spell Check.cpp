#include<bits/stdc++.h>
using namespace std;
int main (){
    int t;cin>>t;
    while (t--){
        int n;cin>>n;
       string s,x="Timur";
       cin>>s;
       sort(s.begin(),s.end());
       sort (x.begin(),x.end());
       if (s==x){cout<<"YES"<<endl;}
       else{cout<<"NO"<<endl;}
    }
    return 0;
}
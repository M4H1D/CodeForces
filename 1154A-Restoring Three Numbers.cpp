#include<bits/stdc++.h>
using namespace std;
int main(){
    int a,b,c,d;
    cin>>a>>b>>c>>d;
    if(a>=b && a>=c && a>=d){cout<<a-b<<" "<<a-c<<" "<<a-d<<endl;}
    else if(b>=a && b>=c && b>=d){cout<<b-a<<" "<<b-c<<" "<<b-d<<endl;}
    else if(c>=a && c>=b && c>=d){cout<<c-b<<" "<<c-a<<" "<<c-d<<endl;}
    else{cout<<d-b<<" "<<d-c<<" "<<d-a<<endl;}
    return 0;
}
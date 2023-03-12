#include<bits/stdc++.h>
#include<cmath>
#include<algorithm>
using namespace std;
int main(){
    long long x,y;cin>>x>>y;
    if(x==0 && y==0){cout<<"0"<<" "<<"0"<<" "<<"0"<<" "<<0;}
    else if(x>0 && y>0){cout<<"0"<<" "<<x+y<<" "<<x+y<<" "<<"0";}
    else if(x<0 && y<0){cout<<-abs(x+y)<<" "<<"0"<<" "<<"0"<<" "<<-abs(x+y);}
    else if(x<0 &&y>0){x=abs(x);cout<<-abs(x+y)<<" "<<"0"<<" "<<"0"<<" "<<abs(x+y);}
    else if(x>0 && y<0){y=abs(y);cout<<"0"<<" "<<-abs(x+y)<<" "<<abs(x+y)<<" "<<"0";}
    return 0;
}
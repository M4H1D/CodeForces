#include<bits/stdc++.h>
#include<cmath>
#include<algorithm>
using namespace std;
int main(){
    int a,b,c,d,e,num=0;
    cin>>a>>b>>c>>d>>e;
    for(int i=1;i<e+1;i++){
        if (i%a==0||i%b==0||i%c==0||i%d==0){num++;}
    }cout<<num;
    return 0;
}
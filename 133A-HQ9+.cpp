////////////<786>//////////////
////[_PUTIN Still Alive_]////
//////Let's rock and Roolllll/////////

#include<bits/stdc++.h>
#include<cmath>
#include<string>
using namespace std;
int main(){
    string s;
    int i,num=0;
    cin>>s;
    for (i=0;i<s.length();i++){
        if(s[i]=='H'||s[i]=='Q'||s[i]=='9'){num++;}
    }
    if(num>=1){cout<<"YES";}
    else{cout<<"NO";}
    return 0;
}

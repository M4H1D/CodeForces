/*
#include<BISMILLAHIR RAHMANIR RAHIM>
#include<Vladimir Putin>
#define Putin_still_Alive 1/0
pip install Putin_er_Khel
Loading..############################## 99%
Download Successfully ...
//"Let's Rock & Roll ;)  "
*/

#include<bits/stdc++.h>
#include<cmath>
#include<algorithm>
#include<math.h>
using namespace std;
int main(){
  int t,x,y,n,mod;
	cin>>t;
	while(t--){
		cin>>x>>y>>n;
        mod=n%x;
		if (n-mod+y<=n){cout<<n-mod+y<<endl;} 
        else {cout<<n-mod-(x-y)<<endl;}
        }
	
	return 0;
}
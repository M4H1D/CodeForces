////////////<786>//////////////
////[_PUTIN Still Alive_]////
//////Let's rock and Roolllll/////////

#include<bits/stdc++.h>
#include<cmath>
using namespace std;
int main(){
    long long int n,k,odd,result;
    cin>>n>>k;
    if (n%2==0){odd=n/2;}
    else{odd=(n/2)+1;}
    if(k<=odd){result=(k*2)-1;}
    else{result=(k-odd)*2;}
    cout<<result;
    return 0;
}
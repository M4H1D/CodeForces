#include <iostream>
#include<cmath>
#include<algorithm>

using namespace std;
int main(){
    int t,bactaria=0;
    cin>>t;
    while(t>0){
        if(t%2==1){bactaria+=1;}
        t=t/2;
    }cout<<bactaria;
    return 0;
}
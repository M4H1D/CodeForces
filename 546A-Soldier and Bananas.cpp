#include <iostream>
using namespace std;
int main(){
 int k,n,w,x=0;
 cin>>k>>n>>w;
 for(int i=1;i<=w;i++){
    x=x+(i*k);
 }
 if(n>=x){cout<<0;}
 else{cout<<x-n;}

    return 0;
}
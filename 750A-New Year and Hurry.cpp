#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,k;cin>>n>>k;
    int baki=240-k;
    int korbe=0,koita=0;
    if(1<=n && n<=10 && 1<=k && k<=240){
        for(int i=1;i<n+1;i++){
            korbe+=(5*i);
            if (baki>=korbe){koita++;}
        }
    }cout<<koita;
    return 0;
}
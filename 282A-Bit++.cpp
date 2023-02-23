#include <iostream>
#include <string>
using namespace std;
int main(){
    int t,x=0;
    string s;
    cin>>t;
    while(t--){
        cin>>s;
        if (s[1]=='+'){
            x+=1;
        }else{x--;}
    }
    cout<<x<<endl;
    return 0;
}
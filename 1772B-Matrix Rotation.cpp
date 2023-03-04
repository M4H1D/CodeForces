#include<bits/stdc++.h>
using namespace std;
int main(){
int a,b,c,d,t,e;
cin>>t;
 while(t--){
        cin>>a>>b>>c>>d;
                if(a<b&&c<d&&a<c&&b<d)
                cout<<"Yes"<<endl;
                 else{e=a;a=b;b=d;d=c;c=e;
                     if(a<b&&c<d&&a<c&&b<d)
                     cout<<"Yes"<<endl;
                        else {e=a;a=b;b=d;d=c;c=e;
                             if(a<b&&c<d&&a<c&&b<d)
                             cout<<"Yes"<<endl;
                                else {e=a;a=b;b=d;d=c;c=e;
                                     if(a<b&&c<d&&a<c&&b<d)
                                     cout<<"Yes"<<endl;
                                        else
                                         cout<<"No"<<endl;
                                         }}}}
                                             return 0;
                                             }

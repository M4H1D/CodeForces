#include <stdio.h>
int main(void) {
	int t,n;
	scanf("%d %d",&n,&t);
	while(t--){
		if((n%10)==0){
			n/=10;
		}else{
			n-=1;
		}
	}
	printf("%d",n);
	return 0;
}
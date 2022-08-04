#include <stdio.h>
#include<math.h>
void main(){
	int r1=8,c1=8,r2=24,c2=24,i,j,c=1,k=0;float pix[64];
	
	float arr[8][8]={{31.25, 30.5, 30.25, 31.0, 30.25, 30.5, 30.75, 31.5}, 
					 {30.5, 31.25, 30.75, 31.0, 31.25, 31.25, 32.0, 32.25}, 
					 {30.5, 30.5,30.75, 31.0, 31.0, 31.5, 32.75, 33.0}, 
					 {31.5, 30.5, 31.0, 30.5, 31.0, 32.25, 33.25, 33.0}, 
					 {30.75, 31.0, 30.5, 30.75, 30.75, 32.0, 31.75, 32.5}, 
					 {31.0, 30.75, 30.75, 31.25, 30.75, 31.75, 32.25, 31.25}, 
					 {31.5, 31.25, 31.5, 30.75, 31.25, 31.25, 31.5, 31.0}, 
					 {31.0, 30.75, 30.75, 30.75, 30.25, 30.75, 30.25, 30.25}};
	float temp[24*24];
	/* code to convert 2D array to 1D array*/
	for(i=0;i<8;i++){
		for(j=0;j<8;j++){
			pix[k]=arr[i][j];
			k++;
		}
	}
	printf("...........pix array..................\n");
	for(i=0;i<64;i++){
		if(i%8==0){
    		printf("\n");
		}
		printf("%.1f ",pix[i]);
	}
	printf("\n\n");
	/*  nearest neighbour interpolation*/
	double r_ratio = r1/(double)r2 ;
    double c_ratio = c1/(double)c2 ;
    double px, py ;
    printf("................Interpolated matrix.................\n");
    for (i=0;i<c2;i++) {
        for (j=0;j<r2;j++) {
            px = floor(j*r_ratio) ;
            py = floor(i*c_ratio) ;
            temp[(i*r2)+j] = pix[(int)((py*r1)+px)] ;
        }
    }
    for(i=0;i<(24*24);i++){
    	if(i%24==0){
    		printf("\n");
		}
		printf("%.1f ",temp[i]);
	}
}

//Question 15 - Lattice Paths

#include <string>
#include <iostream>

#define X_DIM 21 //dim 2 = 1x1 box (2 points per 1 line)
#define Y_DIM 21


int main() {
	long box[Y_DIM][X_DIM] = {};
	
	for(int y = 0; y<Y_DIM; y++) {
		for(int x = 0; x<X_DIM; x++) {
			
			if (y == 0) {
				box[0][x] = 1; //top row of xs
			}
			if (x == 0) {
				box[y][0] = 1; //left row of ys
			}
			if( (x > 0) && (y > 0) ) {
				box[y][x] = box[y-1][x] + box[y][x-1]; //interior conditions
			}
		}
	}
	
	for(int y = 0; y<Y_DIM; y++) { //check box output
		for(int x = 0; x<X_DIM; x++) {
			std::cout << box[y][x];
		}
		std::cout << std::endl;
	}
	std::cout << box[20][20] << std::endl; //final answer
}

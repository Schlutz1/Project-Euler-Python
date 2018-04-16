//Question 28 - Number Spiral Diagonals

#include <string>
#include <iostream>

#define X_DIM 1000 //dimensions of spiral + 1 i.e. 4 -> 5x5 spiral
#define Y_DIM 1000


int main() {
	const int spiral_array_length = (X_DIM + 1) * (Y_DIM + 1);
	
	int break_bool = 0, d_sum = 1, init_distance = 2;
	int fin_sum = 1;
	
	while (break_bool != 1) {
		for (int i = 0; i < 4; i++) {
			d_sum += init_distance;
			fin_sum += d_sum;
			//std::cout << d_sum << std::endl;
		}
		if (init_distance == X_DIM) {
			break_bool = 1;
		}
		init_distance += 2;
	}
	std::cout << fin_sum << std::endl;
}

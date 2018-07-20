/*Question 21 - Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

val = 31626

*/

#include <iostream>
#include <vector>

//Step1 - find all the factors of number x
//step2 - sum all the factors of number x = y

//step 3 - find all factors of hte number y
//step4 - sum all the factors of the number y = z

//compare x and z

int find_proper_divisors(int n) {
  
  	int ceil = n / 2;
  	int tmpSum = 0;
	//iterate from 2, to n/2 checking for even division
	for(int d=2; d <= ceil; d++) {
		if(n % d == 0) {
			tmpSum = tmpSum + d;
			
		}	
	}
	tmpSum++; //to acount for 1 being prime
	return tmpSum;
}



int main() {

	std::vector<int> v; //declares a vec of ints to hold vals

	for (int a=2; a <= 10000; a++) {
		int compareValue = find_proper_divisors(a);
		if (a == find_proper_divisors(compareValue) && a != compareValue) {
			v.push_back(a);
			v.push_back(compareValue);
			std::cout << "Value: " << a << ", Value: " << compareValue << std::endl;
		}
	}
	sort(v.begin(), v.end());
	std::vector<int>::iterator it;
	it = unique(v.begin(), v.end());  

	v.resize(distance(v.begin(),it));
	int summ = 0;
	for(int i = 0; i< v.size(); i++) {
		summ = summ + v[i];
	}
	std::cout << "Value: " << summ << std::endl;

	return 0;
}


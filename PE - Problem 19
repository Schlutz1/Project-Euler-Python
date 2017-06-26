//Question 19 - Counting Sundays

#include <string>
#include <iostream>


int main() {
	int counter, leapFlag = 0, dayCounter = 2;
	std::string dayList[] = {"mon", "tues", "wed", "thurs", "fri", "sat", "sun"};
	
	for(int currentYear = 1901; currentYear <= 2000; currentYear++) {
		for(int currentMonth = 1; currentMonth < 13; currentMonth++) {
			//std::cout << dayList[dayCounter % 7] << std::endl;
			if (dayCounter % 7 == 0) {
				counter++;
			}
			if ( (currentMonth == 1) || (currentMonth == 3) || (currentMonth == 5) || (currentMonth == 7) || (currentMonth == 8) || (currentMonth == 10) || (currentMonth == 12) ) {
				// 31 day condition
				dayCounter += 31;
			}
			else if (currentMonth == 2) {
				//feb condition
				if (currentYear % 4 == 0) {
					dayCounter += 29;
				}
				else {
					dayCounter += 28;
				}
			}
			else {
				//30 day condition
				dayCounter += 30;
			}
			//check what day of the month it is
			//check what that day is
			//check if that day is a sunday
		}
		if (currentYear % 4 == 0) {
			dayCounter = dayCounter % 366;
		}
		else {
			dayCounter = dayCounter % 365;
		}
	//std::cout << currentYear << std::endl;
	}
	std::cout << counter << std::endl;
}

#include <iostream>
#include <ctype.h>

using namespace std;

int CreateTable(int size){

	for (int c = 0;c < size;c++){
		cout << "=";
		if (c == (size - 1)){
			cout << endl;
		}
	}

}

int ShowMultipleTable(int num_multiple){

	int num_multiple;	

	CreateTable(50);

	cout << "Type a Multiple table number to show: ";
	cin >> num_multiple;

	system("clear");

	CreateTable(50);
	
	for (int c = 0;c > 10;c++){
		cout << num_multiple << " X " << c << " = " << num_multiple + c;
		cout << endl;
	}
	return 0;
}

int main(){

	cout << isdigit(1);
	cout << endl;

	return 0;
}

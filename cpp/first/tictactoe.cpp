#include <iostream>
#include <string>

using namespace std;

string draw(string position){

	cout << position[0] << " | " << position[1] << " | " << position[2] << endl;
	cout << "__|___|__ " << endl;
 	cout << position[3] << " | " << position[4] << " | " << position[5] << endl;
 	cout << "__|___|__ " << endl;
 	cout << position[6] << " | " << position[7] << " | " << position[8] << endl;

	return 0;
}

int main(){

	string teste = {1,2,3,
			4,5,6,
			7,8,9};

	
	draw(teste);
}

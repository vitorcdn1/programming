#include <iostream>
#include <string>

using namespace std;

string draw(string position){

	cout <<   position[0] << " | " << position[1] << " | " << position[2]  << endl;
	cout << "__|___|__ " << endl;
 	cout << "4 | 5 | 6 " << endl;
 	cout << "__|___|__ " << endl;
 	cout << "7 | 8 | 9 " << endl;

	return 0;
}

int main(){

	string teste[5] = {"x","o","x"};

	draw(teste);
	return 0;
}

#include <iostream>

using namespace std;


int learn(int num){
	
	int result, response;

	for (int c = 0;c < 9;c++){
		result = num * c;

		cout << num << " X " << c << " = ";
		cin >> response;

		if (response == result){
			cout << "Parabens vc acertou\n";
		}
		else{
			cout << "Você errou";
		}
	}

	return 0;
}

int main(){

	int response, multiple_table_num;

	for (int c = 0;c < 50;c++){
		cout << "=";
		if (c == 49){
			cout << "\n";
		}
	}
	
	cout << "1 - Exit the program" << endl;
	cout << "2 - Learn A new multiple table" << endl;
	for (int c = 0;c < 50;c++){

		cout << "=";
		if (c == 49){
			cout << "\n";
		}
	}


	cout << "Type a option: ";
	cin >> response;

	if (response == 1){
		return 0;
	}
	else {

		cout << "Type the number of the multiple table that you wish to learn: ";
		cin >> multiple_table_num;

		learn(multiple_table_num);
	}

	return 0;
}

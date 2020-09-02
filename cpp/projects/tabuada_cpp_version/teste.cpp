#include <iostream>
#include <string>

using namespace std;

bool ReadInt(string teste){

        bool stop = false;
        int c = 0;

        while (stop == false){

                if (c == teste.length()){
                        stop = true;
                }
                else {
                        if (isdigit(teste[c]) == false){
                                return false;
                        }
                }

                c++;
        }

        return true;
}

int main(){

        string something;

        cout << "Type something: ";
        cin >> something;

        bool validation = ReadInt(something);

        if (validation == true){
                cout << "O valor digitado e um número";
        }
        else {
                cout << "O valor digitado não é um número";
        }

	cout << endl;
	return 0;
}

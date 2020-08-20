#include <iostream>

using namespace std;

int main(){
        
        int response;

        for (int c = 0;c < 50;c++){
                cout << "=";
        }

        cout << "1 - Exit The program\n";
        cout << "2 - Learn a new multiplication table\n";

        for (int c = 0;c < 50;c++){
                cout << "=";
        }

        cout << "Type one option: "
        cin >> response;

        if (response == 1){
                return 0;
        }
        elif (response == 2){
                cout << "You pressed option 2";
        }
        else{
                
        }

        cout << "\n";
        cout << "\n";
        return 0;
}
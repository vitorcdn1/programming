#include <iostream>
#include <string>

using namespace std;

int main(){

        int num1, num2, result;
        string myFirst = "Hello World\n";
        string name;

        cout << "type your name: ";
        cin >> name;

        if (name.length() == 5){
                cout << "Hello Vitor";
        }
        else {
                cout << name.length();
        }

        cout << "\n";
        return 0;
}
#include <iostream>
#include <string>
#include <array>

using namespace std;

int PrintUnderline(int max = 10){

        for (int c = 0;c < max;c++){
                cout << '_';
                if (c == max-1){
                        cout << endl;
                }
        }

        return 0;
}

int draw(){

        return 0;
}

int main(){

        array<int, 3> foo[] = {10, 20, 30};

        for (int c = 0;c < foo.size();c++){

                cout << foo[c] << endl;
        }

        cout << foo[0] << endl;

	PrintUnderline(20);

        return 0;
}

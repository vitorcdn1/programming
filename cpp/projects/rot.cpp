#include <iostream>
#include <string>
#include <ctype.h>

using namespace std;

int encrypt(string palavra){

	string alphabeto = "ABCDEFGHIJKLMNOPQRSTUVWXZ";
	int ReturnWord[palavra.length()];
	string final_word[palavra.length()];

	for (int c = 0;c < palavra.length();c++){
                for (int x = 0;x < alphabeto.length();x++){
                        if (palavra[c] == alphabeto[x]){
				 ReturnWord[c] = x;
                            
                                int aumentar;
                                
                                for (int a = 0;a < 13;a++){
                                	if (a == 0){
                                		aumentar = ReturnWord[c];
                                	}
                                	else {
                                		if (aumentar == 25){
                                			aumentar = 0;
                                		}
                                		aumentar++;
                                	}
                                }
                                
                                ReturnWord[c] = aumentar;
                        }
                }
	}
	
	for (int c = 0;c < palavra.length();c++){
		cout << alphabeto[ReturnWord[c]];
	}
	
	cout << endl;
	return 0;
}

int main(){

        cout << encrypt("VITOR");
	
	cout << endl;
	
	return 0;
}

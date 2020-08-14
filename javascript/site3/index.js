function readoption(question="write a number: ",array_list=[]){

	var array_numbers;

	if (array_list == []){

		for (var c = 0;c < array_list.length;c++){
			array_numbers[c] = c
		}
	}

	
	while (true){

		var response = Number(window.prompt("Write a number: "))

		if (Number.isInteger(response) == true && response in array_numbers){
			return response
		}
		
		else {
			if (Number.isInteger(response) == false){
				window.alert("Please write a integer number !!")
			}
			if (response in array_numbers == false){
				window.alert("Please write a number in the options")
			}

		}
	}
}

var list = [
	"Exit program",
	"Digitar algum número"
	]

readoption(list)

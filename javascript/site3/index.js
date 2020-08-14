function readoption(question="write a number: ",array_list=[]){

	while (true){

		var response = Number(window.prompt("Write a number: "))

		if (Number.isInteger(response) == true && response in array_list){
			return response
		}
		if (array_list == [] && Number.isinteger(reponse) == true){

			return response
		}
		if (response == NaN){
				
			window.alert("Please write a integer number !!")
		}

	}
}

var list = [
	"Exit program",
	"Digitar algum número"
	]

readoption(list)

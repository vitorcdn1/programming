function CreatTable(){
	
	var Name = window.prompt("Type your name: ")
	var Lname = window.prompt("Type your Last Name: ")
	var age = window.prompt("Type your age: ")

	var teste = {
		FirstName: Name,
		LastName: Lname,
		Age: age
	}

	for (x in teste){
		console.log(teste[x])
	}
}

function TestFunction(){

	var teste = document.getElementsByTagName("body")

}

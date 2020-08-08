var rubiks = {type: "gans-356",
		model: "3x3x3"}

function teste(){
	
	var increase = 0
	var biggest = 0

	for (x in rubiks){
		
		if (x.length >= biggest){
			biggest = x.length
		}

		increase += 1
	}

	for (x in rubiks){
		console.log(x.concat(" ").concat(x.length))
	}

}

teste()

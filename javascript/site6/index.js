function ChangeSomething(){

        var teste = "vitor"

        var thesomething = document.getElementsByTagName("p")

        
        for (x in thesomething){
                console.log(thesomething[x].innerHTML)
        }

        for (var x = 0;x < thesomething.length;x++){

                console.log(thesomething[x].innerHTML)

                if (x == 1){
                        thesomething[x].innerHTML = "You are special"
                }
                else{
                        thesomething[x].innerHTML = "The brand-new inner html"
                }
        }
}

function ChangeImage(){
        var image = document.getElementById("ThisIsTheImageId").src

        var path = image.slice(image.lastIndexOf("/") + 1, image.length)

        console.log(path)

        if (path == "TheFirstImage.jpeg"){

                document.getElementById("ThisIsTheImageId").src = "TheSecondImage.jpeg"
                document.getElementById("result").innerHTML = "Python Image"
                document.getElementById("result").style.backgroundColor = "blue"
        }
        else{
                document.getElementById("ThisIsTheImageId").src = "TheFirstImage.jpeg"
                document.getElementById("result").innerHTML = "Javascript Image"
                document.getElementById("result").style.backgroundColor = "yellow"
        }

}

function ChangeTest(){
        var image = document.getElementsByTagName("body")[0].style.backgroundColor = "purple"

        console.log(image)
}

function MouseIsOver(){

        console.log("The Mouse is over")
        var change = document.getElementsByTagName("p")[0].style.color

        console.log(change)
}

function MouseOut(){
        console.log("The Mouse is Out")
}

var id_button = document.getElementById("result")

id_button.addEventListener("keydown", ChangeImage)
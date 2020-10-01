function GeneratePass(tamanho = 30, lower = true, upper = true, num = true){

        if (lower == false && upper == false && num == false){
                return "Error"
        }

        var alphabeto = "abcdefghijklmnopqrstuvwxyz"
        var return_list = []
        var pass = []
        var siz = return_list.lenght

        while (siz != tamanho){

                while (true){
                        x = Math.floor(Math.random() * 3)

                        if (x == 0){
                                if (lower == true){
                                        return_list[return_list.length] = alphabeto[Math.floor(Math.random()*26)]
                                        break
                                }
                        }

                        if (x == 1){
                                if (upper == true){
                                        return_list[return_list.length] = alphabeto.toUpperCase()[Math.floor(Math.random() * 26)]
                                        break
                                }
                        }
                        if (x == 2){
                                if (num == true){
                                        return_list[return_list.length] = String(Math.floor(Math.random() * 9))
                                        break
                                }
                        }
                }

        }

        console.log(return_list)

        for (var c = 0;c < return_list.length;c++){
                document.write(return_list[c])
        }
}
//restart
var button_restart = document.querySelector("#button");

//grab squares
var squares = document.querySelectorAll("td");

//clear squares
function clearBoard(){
    for (let index = 0; index < squares.length; index++) {
        squares[index].textContent = "";
        
    }
}
button_restart.addEventListener('click', clearBoard())

//check square marker
function changeMarkerX(){
    this.textContent = "x";
       
}
function changeMarkerO(){
    this.textContent = "O";
}
for(var i =0; i<squares.length; i++){
    squares[i].addEventListener('click',changeMarkerX)
}
for(var i =0; i<squares.length; i++){
    squares[i].addEventListener('dblclick',changeMarkerO)
}
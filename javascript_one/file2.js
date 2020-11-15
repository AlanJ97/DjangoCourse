var roster = [];
function addNew(){
    var newName = prompt("YOur name: ");
    roster.push(newName);
}
function remove(){
    var remName = prompt("YOur name to remove: ");
    var index = roster.indexOf(remName);
    roster.splice(index,1);
}
function display(){
    console.log(roster);
}

var start = prompt("Shall we begin? y/n");
var request = "empty";

if (start === "y"){
    while(request !== "quit"){
        request = prompt("Choose either add, remove, display or quit")
        if(request === 'add'){
            addNew();
        }
        else if(request === 'remove'){
            remove();
        }
        else if(request === 'display'){
            display();
        }
    }
    alert("BYE")
}
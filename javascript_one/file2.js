var firstName = prompt("Your firstname");
var lastName = prompt("Your lastname");
var age = prompt("Your age");
var height = prompt("YOur height");
var petName = prompt("Your pet name");

var nameCond = null;
var ageCond = null;
var heightCond = null;
var petCond= null;

//Name condition
if(firstName[0] === lastName[0]){
    nameCond = true;
}
else{
    nameCond = false;
}

//AGe condition
if(age > 20 && age < 30){
    ageCond = true;
}
else{
    ageCond = false;
}

//height condition
if(height <= 170){
    heightCond = true;
}
else{
    heightCond = false;
}

//pet condition
if(petName[petName.length-1] === "y"){
    petCond = true;
}
else{
    petCond = false;
}

//all conditions
if(nameCond && ageCond && heightCond && petCond){
    console.log("You passed")
}
else{
    console.log("You don't pass")
}
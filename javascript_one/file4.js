var employee = {
    name : "Alan Jesús",
    job : "President",
    age: 31,
    nameLength: function (){
        console.log(this.name.length);
    }
}

var employee2 = {
    name : "Alan Jesús",
    job : "President",
    age: 31,
    report: function (){
        alert("name is " + this.name + " job is "+ this.job+ " age is "+ this.age);
    }
}

var employee3 = {
    name : "Alan Jesús",
    job : "President",
    age: 31,
    lastname: function (){
        console.log(this.name.split(" ")[1]);
    }
}


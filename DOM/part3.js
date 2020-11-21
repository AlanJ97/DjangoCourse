var headOne = document.querySelector("#one")
var headTwo = document.querySelector("#two")
var headThree = document.querySelector("#three")

headOne.addEventListener( 'mouseover', function(){
    headOne.textContent = "Mouse Is over now";
    headOne.style.color = 'blue'
})

headOne.addEventListener('mouseout', function(){
    headOne.textContent = "HOver over me";
    headOne.style.color = "black";
})

headTwo.addEventListener("click", function(){
    headTwo.textContent = "I was clicked";
    headTwo.style.color = "green";
})

headThree.addEventListener("dblclick", function(){
    headThree.textContent ="I was double clicked";
    headThree.style.color ="purple";
})
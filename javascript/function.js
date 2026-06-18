Function Definition
    1. function declaration
    2. function expression
    3. arrow function
    4. callback function
    5. higher order function
    6. Anonymous funciton


Normal Funtion:
---------------
function functionname(){
    //statement
}

functionname()

function greet(){
    console.log("Welcome to  javascript Funciton ")
}

greet()


// Anonymous funciton
// -------------------
const name=10
console.log(typeof name)


const sample = function (){
    console.log("I am Announymous Function")
}

console.log(typeof sample)
sample()


// arrow function
// ---------------

Syntax:
() => expression


const add = () => console.log("welcome")
c=add()

const add = () => {console.log("welcome")}
c=add()


// callback function:
// --------------------

setTimeout(myfunction,2000)
console.log("hi")

function myfunction(){
    console.log("I am example for Callback Function")
}


function greet(func){
    console.log("hi")
    func()
}
function display(){
    console.log("i am callback function")
}

greet(display)




function outer(){
    console.log("Outer Function")
    return function inner(){
        console.log("I am inner Function")
    }
    
}

const test=outer()
console.log(typeof test)
test()










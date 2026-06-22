REST, SPREAD , DESTRUCTING

REST :  Packing rest of the Element
SPREAD :  Unpack or expand

REST: function,Destructing
SPREAD:  Array, object

[...]

// SPREAD:
// -------
//     1. Combining Arrays
//     2. copying Object
//     3. Passing Argument to function


const primary_color=["Red","blue","green"]
const allcolors=[...primary_color,"orange","pink","purple"]
console.log(primary_color)
console.log(allcolors)


const fruits=["apple","banana","guava"]
const vegetables=["tomato","potato","carrot"]
const combined=[...fruits,...vegetables]
console.log(combined)

const user={name:"isai",age:21};
const address={...user,city:"Chennai"};
console.log(address)

const user={name:"isai",age:21};
const address={city:"Chennai"};
const person_details={...user,...address}
console.log(person_details)


function calculateTotal(v1,v2,v3){
    return v1+v2+v3
}

const numb=[10,20,30];
console.log(calculateTotal(...numb))

// REST:
// -----
// Collect rest of the values into Single variable

// uses:
//     1. function Defintion
//     2. Destructing


function sample(a,b,...numb){
    console.log(a)
    console.log(b)
    console.log(numb)
}
sample(1,2,3,4,5)


// Destructuring
// --------------
// Unpack value from array or properties from object  into distinct variable

// object Destructuring

const person={ firstname:"Kiruthika",password:"test@123"}
// const first_name=person.firstname
// const password=person.password
// console.log(first_name,password)
const {firstname,password}=person;
console.log(firstname,password)
const {firstname : fname ,password :pwd}=person;
console.log(fname,password)

const rgb=["red","green","blue"]
const [r,g,b] =rgb;
console.log(r)

const rgb=["red","green","blue"]
const [r,,b] =rgb;
console.log(b)

let a=10;
let c=20;
[a,c]=[c,a]
console.log(a,c)



// REST in Destructing
// --------------------

const color=["red","blue","green","yellow","pink","white"]
const [r,b,...restcolor]=color
console.log(restcolor)
console.log(r)
console.log(b)


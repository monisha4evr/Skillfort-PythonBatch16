console.log("I am from External Script file")
a=10
console.log(`a value is ${a}`)

Data Types:

1. Primitive (Single value)
2. non primitive (collection)

Number
String
Boolean
float
null
undefined
NaN

Scope
var , let , const 
var => Global/Functional scope
let , const = > Block Scope

var
1. scope : Global/functional 
2.  can redeclare
3.  can reassign
4.  hoisting allow
5.  initailize not mandatory
 
var a=10
var a=20

let :
1. scope : Block 
2. can't redeclare
3. can reassign
4. hosisting not allow (TDZ)
5. initailize not mandatory


let a=10;
 a=20;

const:
1. Scope:Block
2.cant redeclare
3.can't Reassign
4.hosisting not allow (TDZ)
5. initailize mandatory


const a=10;
const a=20;


Hoisting:


console.log(a)
b=10



const a=10;
console(a)

Based on Variable Declaration
1. Global Scope
2. Functional Scope
3. Block Scope

const a=10;
function fname(){
    let b=20;
    if(1){
        
        console.log("B value is"+b)
    }
    console.log(b)
    console.log(a)
}
fname()


//type coercion 
1. implicit
2. explicit Number(),string()

a=15-"12"
console.log(a)

a="abc"+12+3
console.log(a)

a=12+5+"abc"
console.log(a)












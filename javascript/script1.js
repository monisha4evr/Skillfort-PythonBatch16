/* Scope
     1. Global Scope
     2. Functional Scope
     3. Block Scope  */

const a=10;
a=20;


DataType:

 int 
 float 
 string 

var a="123a"

 null 
 undefined

 NaN


function sample(){
    a=20
    if(true)
    {
        a=30
        console.log("inside if "+a)
    }
    console.log("function block" + a)
}
console.log("Outer" + a)
sample()


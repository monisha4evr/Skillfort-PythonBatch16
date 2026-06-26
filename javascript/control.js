if
if else
if else if
switch

if 

Syntax:

if(consition){
    // if block
}

let age=18;
if(age>=18){
    console.log("you are eligible to vote")
}


if  else

Syntax:
if(condition){
    //true Block
}
else{
    // else block
}

let age=18;
let voter_id=false
if( age>=18 && (voter_id)){
    console.log("you are eligible to Vote")
}else{
    console.log("you are not Eligible")
}

if else if 

//Syntax:
if(cond1){
    //if block
}else if(cond2){
    // else if block
}
else{
    //else block
}

let a=30;
let b=45;
let c=20;
if(a>b && a>c){
    console.log("A is Biggest")
}else if(b>c){
    console.log("B is Biggest")
}else{
    console.log("C is Biggest")
}

switch(exp){
     case cond1:
        //Statement
        break;
    case cond2:
        //statement
        break;

    default:
            //statement
            break;

}
   

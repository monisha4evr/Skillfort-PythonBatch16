Loops 
1.for 
2. while 
3. do -while 

For Loops
Syntax:

for(exp1;exp2;exp3){
    // Statement
}

exp1 => initialization
exp2 => Condition 
exp3 => increment/decrement 



for(let i=1;i<=5;i++){
    console.log(i)
}

for(let i=5;i>=1;i--){
    console.log(i)
}

let i=1;
for(;i<=5;i++){
    console.log(i)
}

for(let i=1;i<=5;){
    console.log(i);
    i++;
}

a=["apple","orange","banana"]

for(let i in a){
    console.log(i)
}

for(let j of a){
    console.log(j)
}

while
----- 
Syntax:
--------
initialization;
while(cond){
    increment/decrement
}


let i=5;
while(i>=1){
    console.log(i);
    i--;
}

do while
--------
Syntax:

initialization
do{
    increment/decrement
}while(condi)


let i=0;
do{
    console.log(i);
    i++
}while(i<=5)



for(let i=1;i<=5;i++){
    if(i==3){
        break
    }
    console.log(i)
}

// i=1 => 1<=5 T i=2
//      1==3 F   => 1
// 2<=5 T i=3
//      2==3 F => 2
// 3<=5 T i=4
//      3==3 T = break---

for(let i=1;i<=5;i++){
    if(i==3){
        continue;
    }
    console.log(i)
}

// i=1 => 1<=5 T i=2
//      1==3 F   => 1
// 2<=5 T i=3
//      2==3 F => 2
// 3<=5 T i=4
//      3==3 T =  Skip
// 4<=5 T i=5
//      4==3 F => 4
// 5<=5 T i=6
//      5==3 F => 5
// 6<=5 F
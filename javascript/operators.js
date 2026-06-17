Operators
1. Arithmetic (+,-,*,/,%,**, ++,--)
2. Assignment (==,+=,-=,*=,/=,%=)
3. Comparision (>,<,>=,<=,==,!=,===,!==)
4. Logical (and => && , or || , not !)
5. bitwise

a=10
b=15
c=a+b
console.log(c)
console.log(10-5)
console.log(10*3)
console.log(10/2)
console.log(11/2)
console.log(2**3)

//++ , -- 

let a=10;
a++
console.log(a)


// Cant reassign
// const a=10;
// a++
// console.log(a)


a=10;
b=--a
d=15
c=d--
console.log(b,c)
console.log(d)

console.log(5==5)

a=10
a+=1
console.log(a)

// == vs ===

a=5
b='5'
console.log(a==b)
console.log(a===b)


// Logical
// -------

a=5;
b=10;
c=2;
console.log(a>b && a>c) // 5>10
console.log(a>b || a>c) // 5>10 F 5>2 T

console.log(10 || 0 )

// Nullish coalescion(??)
a=null
console.log( a ?? "apple")

a="user1";
console.log(a ?? "Guest")

a=101
console.log(a ?? "Guest")

a="";
console.log(a??"banana")

a=0;
console.log(a??"orange")

a=0;
console.log(a||"Banana")

a=true;
console.log(a||"carrot")


// falsy or truthy

//Falsy
0
false
"",'',``
null
undefined
NaN

Truthy
[]
{}

console.log(0 == false)

console.log([] == false)
[]=>""=>0 == 0

console.log([]==[])
console.log([]===[])

console.log({} === {})

console.log(null == undefined)  // True
console.log(null === undefined) // False

console.log(null==false)



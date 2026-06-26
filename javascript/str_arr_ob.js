// 1. arrow function
// 2. Closure 
// 3. string 
//     1.uppercase,lowercase,length,slice,replace,split,includes,indexOf,lastIndexOf,charAt,concat
// 4. array - types , push,unshift,pop,shift,splice,indexOf,includes
//         methods - map filter reduce 
        
// 5. object

// 6.rest,spread,destructuring  Tommorow

// Arrow Function

const greet = ()=> console.log(" Welcome to Arrow Function")
greet()

const sample = x => { console.log(x*2)}
sample(5)


let x=10;
let y=15;

const add = (a,b) => { return a+b }
z=add(x,y)
console.log(z)

// closure

function outer(){
    function inner(){
        console.log("Welcome")
    }
    inner()
}

outer()

function outer(){
    function inner(){
        console.log("Welcome")
    }
    return inner
}

const inr=outer()
inr()

function outer(){
    let a=0;
    function inner(){
        console.log(a++)
    }
    return inner
}

const inr=outer()
inr()
inr()


//string

let a=" I am Learning Javascript ";
console.log(a)
console.log(a[5])
console.log(a.toUpperCase())
console.log(a.toLowerCase())
console.log(a)
console.log(a.trim())
console.log(a.length)
console.log(a.replace("Learning","Loving"))
console.log(a.split(" "))
console.log(a.slice(5,13))

// array
// Indexed
//collection of data 
// store same or mixed kind of data
// 1D / 2D 

a=[1,2,3,4]
console.log(a[0])

for(let i of a){
    console.log(i)
}


a=[1,2,3,4]
a.push(5)
a.unshift(9)
console.log(a)

b=[1,2,3,4]
b.pop()
b.shift()
console.log(b)

// Syntax: splice(start, delete_count, replace)

const c=["apple","orange","banana"]
console.log(c.splice(0,1))
console.log(c.splice(1,1,'mango','grapes',"carrot"))
console.log(c.includes("orangess"))

a=[
    [1,2,3], // row 0
    [4,5,6], // row 1
    [7,8,9]  // row 2
]
console.log(a[1][1])


a=[1,2,3,4,5]
console.log(a.map((i)=>{return i*5 }))  
console.log(a.filter((i)=>{return i%2==1}))
console.log(a.reduce((i,n)=>{return i+n},5))



// object:
// -------

const fruits={
    "name":"apple",
    "type":"Sweet",
    "price_range":[100,150,200],
    "myfunc":function (){ return("i am inside the Object")}
}

console.log(fruits)
console.log(fruits.name)
console.log(fruits.price_range)
console.log(fruits['type'])
sample=fruits['myfunc']
console.log(sample())

















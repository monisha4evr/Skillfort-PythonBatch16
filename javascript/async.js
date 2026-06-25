async function fname(){
    return("I am Function")
}

console.log(fname())


const test=new Promise((resolve,failure)=>{
    setTimeout(()=>{
        console.log("hi")
    },2000)
})

test.then()





 async function getdata(){
    const res=await fetch('https://fakestoreapi.com/products/1')
    const data=await res.json()
    console.log(data)
 }

 getdata()




fetch('https://fakestoreapi.com/products/1')
.then(result=>result.json())
.then(data=>console.log(data))

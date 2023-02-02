interface stu{
    id:number,
    age:number
}

interface tech {
    clas:string,
    name:string

}

type total=stu | tech


let obj:total={
    clas:"abc",
    name:"good",
    id:99
    
}

console.log(obj)

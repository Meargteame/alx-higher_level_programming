#!/usr/bin/node



const args = process.argv;   
const myNumber = parseInt(args[2])
console.log(typeof(myNumber))
if ((!isNaN(args[2]))){
    console.log('My number : ' + myNumber)
}

else  {
console.log('Not a number') 
  }


#!/usr/bin/node
const args = process.argv;
const num = args[2] ;

function factorial(num){
    if(num == 0 || num ==1 ||NaN){
        return 1;
    }

    return num * factorial(num - 1)
}
console.log(factorial(num))
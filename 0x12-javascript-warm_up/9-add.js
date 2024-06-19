#!/usr/bin/node 
/**
 * Write a script that prints the addition of 2 integers

The first argument is the first integer
The second argument is the second integer
You have to define a function with this prototype: function add(a, b)
You must use console.log(...) to print all output
You are not allowed to use var
 */

const args = process.argv;
const a = parseInt(args[2])
const b = parseInt(args[3])


function add(a, b){
    console.log(a+b)
}
add(a,b)

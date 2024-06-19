#!/usr/bin/node
/**
 * Write a script that prints two arguments passed to it, in the following format: “ is ”

You must use console.log(...) to print all output
You are not allowed to use var
 */

const args = process.argv;     
if (args[2] || args[3]){
    console.log(args[2] + ' is ' + args[3]) 
}

else {
console.log(args[2] + ' is ' + args[3]) 
  }

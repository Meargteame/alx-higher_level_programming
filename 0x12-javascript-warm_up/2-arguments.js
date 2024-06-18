#!/usr/bin/node
const args = process.argv;     
if (!args[2]){
    console.log('No argument') // no argument is passed 
}
else if  (args[2]){
console.log('Argument found') // if 1 argumenet is passed 
   
}
else{
 console.log('Argument found') // otherwise
}

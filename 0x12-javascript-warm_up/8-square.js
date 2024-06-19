#!/usr/bin/bash
/**
 * Write a script that prints a square

The first argument is the size of the square
If the first argument can’t be converted to an integer, print “Missing size”
You must use the character X to print the square
You must use console.log(...) to print all output
You are not allowed to use var
You must use a loop (while, for, etc.)
 */


const args = process.argv;   
const size = args[2];

if ((isNaN(size))){
    console.log("Missing size");
}
else{
    for(let i =0;i<size;i++){
        let row =''
        for (let j =0 ; j<size;j++){
            row += 'X';
        }
        console.log(row);
    };
};
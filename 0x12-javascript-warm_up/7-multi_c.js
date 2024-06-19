#!/usr/bin/node
/**
 * 7. I love C
mandatory
Write a script that prints x times “C is fun”

Where x is the first argument of the script
If the first argument can’t be converted to an integer, print “Missing number of occurrences”
You must use console.log(...) to print all output
You are not allowed to use var
You can use only two console.log
You must use a loop (while, for, etc.)
 */

const args = process.argv;   
const noOfOccurences = args[2]

if ((isNaN(noOfOccurences))){
    console.log("Missing number of occurrences")
}
else{
let string = "C is fun"

for(let i=1 ; i<=noOfOccurences ; i++){
    console.log(string)
}

}
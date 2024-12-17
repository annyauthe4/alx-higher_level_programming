#!/usr/bin/node

/*
Searches the second biggest integer in the list of arguments.
You can assume all arguments can be converted to integer.
If no argument is passed, print 0.
If there is only one argument, print 0.
*/

const args = process.argv.slice(2).map(Number); // Convert all arguments to numbers

if (args.length < 2) {
  console.log(0); // If there are less than two arguments
} else {
  const uniqueArgs = [...new Set(args)]; // Remove duplicates
  uniqueArgs.sort((a, b) => b - a); // Sort in descending order

  if (uniqueArgs.length < 2) {
    console.log(0); // If there's no second unique number
  } else {
    console.log(uniqueArgs[1]); // Print the second largest number
  }
}

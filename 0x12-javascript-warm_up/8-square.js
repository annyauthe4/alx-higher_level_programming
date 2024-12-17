#!/usr/bin/node

/*
Prints a square. The first argument is the size of the square
If the first argument can’t be converted to an integer, print 'Missing size'
You must use the character X to print the square.
You must use console.log(...) to print all output
You are not allowed to use var
You must use a loop (while, for, etc.)
*/

const args = process.argv.slice(2);
const num = parseInt(args[0]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
}

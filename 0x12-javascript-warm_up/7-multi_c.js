#!/usr/bin/node

/*
Prints x times C is fun. Where x is the first arg of the script.
If the first argument can’t be converted to an int, print message.
*/
const args = process.argv.slice(2);
const num = parseInt(args);

if (isNaN(args[0]) || args[0] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}

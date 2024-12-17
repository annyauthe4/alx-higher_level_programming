#!/usr/bin/node

/*
Computes and prints the factorial of a number.
The first argument is the integer used for computing the factorial.
If the argument cannot be converted to an integer, the factorial is considered 1.
The calculation is done recursively.
*/

function factorial(n) {
  if (n <= 1) {
    return 1; // Base case for recursion
  }
  return n * factorial(n - 1); // Recursive call
}

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log(1); // If the argument is NaN, print 1
} else {
  console.log(factorial(num)); // Print the result of the factorial function
}

#!/usr/bin/node

// Define the add function
function add (a, b) {
  return a + b;
}

// Export the add function to make it visible outside
module.exports.add = add;

#!/usr/bin/node

// prints the first argument passed to it
const args = process.argv.slice(2);
console.log(args[0] || 'No argument');

#!/usr/bin/node

/*
Imports an array and computes a new array.
A new list must be created with each value equal to
the value of the initial list, multipled by the index in the list
Print both the initial list and the new list.
*/
// Import data
const list = require('./100-data').list;

const newList = list.map((x, index) => x * index);
console.log(list);
console.log(newList);

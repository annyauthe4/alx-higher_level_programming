#!/usr/bin/node

/*
Imports a dictionary of occurences by user id and computes a dictionary
of user ids by occurrence. In the new dictionary:
A key is a number of occurrences
A value is the list of user ids.
Print the new dictionary at the end
*/
// Import dictionary
const dict = require('./101-data').dict;

// Create new dict by requirement
const newDict = {};
for (const [userId, occurence] of Object.entries(dict)) {
  if (!newDict[occurence]) {
    newDict[occurence] = [];
  }
  newDict[occurence].push(userId);
}

console.log(newDict);

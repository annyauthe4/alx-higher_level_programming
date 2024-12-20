#!/usr/bin/node

// Returns the number of occurrences in a list.
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, occurence) => (occurence === searchElement ? count + 1 : count), 0);
};

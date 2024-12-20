#!/usr/bin/node

// Returns the desrever version of a list
exports.esrever = function (list) {
  const desreverList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    desreverList.push(list[i]);
  }
  return desreverList;
};

#!/usr/bin/node

/*
Defines a square and inherits from Square of 5-square.js
Create an instance method called charPrint(c) that prints
the rectangle using the character c.
If c is undefined, use the character X
*/
// Import square class
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    const Char = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(Char.repeat(this.width));
    }
  }
}

module.exports = Square

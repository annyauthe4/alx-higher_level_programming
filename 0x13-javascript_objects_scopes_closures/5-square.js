#!/usr/bin/node

/*
Defines a square and inherits from Rectangle of 4-rectangle.js
use the class notation for defining your class and extends
The constructor of Rectangle must be called (by using super()
*/
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;

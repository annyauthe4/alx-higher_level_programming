#!/usr/bin/node

/*
Define a Rectangle class with a constructor to initialize its values.
If width or height is <= 0, create an empty object.
*/
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

// Export module
module.exports = Rectangle;

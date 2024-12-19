#!/usr/bin/node

/*
Defines a Rectangle class with a constructor that initializes it
only if width and height are > 0.
Uses a print method to print it using X.
*/
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

// Make mode importable outside
module.exports = Rectangle;

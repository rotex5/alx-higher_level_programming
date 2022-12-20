#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let output = c;

    if (output) {
      this.printer(output);
    } else {
      output = 'X';
      this.printer(output);
    }
  }

  printer (shape) {
    let i = 0;

    while (i < this.height) {
      console.log(shape.repeat(this.width));
      i++;
    }
  }
}
module.exports = Square;

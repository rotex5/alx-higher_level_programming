#!/usr/bin/node

const process = require('process');
const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);

if (x && y) {
  console.log(add(x, y));
} else {
  console.log('NaN');
}

function add (a, b) {
  return a + b;
}

#!/usr/bin/node

const process = require('process');
const x = parseInt(process.argv[2]);
let i = 0;
const output = 'X';

if (x) {
  while (i < x) {
    console.log(output.repeat(x));
    i++;
  }
} else {
  console.log('Missing size');
}

#!/usr/bin/node

const process = require('process');
const input = parseInt(process.argv[2]);

if (input) {
  console.log('My number: ' + input);
} else {
  console.log('Not a number');
}

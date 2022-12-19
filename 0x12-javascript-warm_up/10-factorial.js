#!/usr/bin/node

const process = require('process');
const x = parseInt(process.argv[2]);

if (x) {
  console.log(fac(x));
} else {
  console.log(1);
}

function fac (a) {
  if (a < 0) {
    return -1;
  } else if (a === 0) {
    return 1;
  } else {
    return (a * fac(a - 1));
  }
}

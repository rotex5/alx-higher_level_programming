#!/usr/bin/node

const process = require('process');
const tempArr = process.argv.slice(2, process.argv.length);
const newArr = [];

for (let i = 0; i < tempArr.length; i++) {
  newArr.push(parseInt(tempArr[i]));
}

if (process.argv.length < 4) {
  console.log(0);
} else {
  console.log(newArr.sort(function (a, b) {
    return a - b;
  }).reverse()[1]);
}

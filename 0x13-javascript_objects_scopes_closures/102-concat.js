#!/usr/bin/node
const fs = require('fs');
const process = require('process');

const sourceFile1 = fs.readFileSync(process.argv[2]);
const sourceFile2 = fs.readFileSync(process.argv[3]);
const destFile = process.argv[4];

fs.writeFileSync(destFile, sourceFile1 + sourceFile2);

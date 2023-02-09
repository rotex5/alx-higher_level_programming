#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filename = process.argv[3];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }

  fs.writeFile(filename, body, function (err) {
    if (err) {
      console.error(err);
    }
  });
});

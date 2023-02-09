#!/usr/bin/node

const request = require('request');
const url = String(process.argv[2]);

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(`code: ${response.statusCode}`);
});

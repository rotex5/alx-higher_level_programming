#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const resp = JSON.parse(body);

  let counter = 0;
  for (const i of resp.results) {
    for (const urls of i.characters) {
      if (urls.search('18') > 0) {
        counter++;
      }
    }
  }
  console.log(counter);
});

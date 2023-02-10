#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, function (error, _, body) {
  if (error) {
    console.log(error);
  } else {
    const resp = JSON.parse(body).characters;
    outputNames(resp, 0);
  }
});

function outputNames (resp, idx) {
  request.get(resp[idx], function (err, _, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      if (++idx < resp.length) {
        outputNames(resp, idx++);
      }
    }
  });
}

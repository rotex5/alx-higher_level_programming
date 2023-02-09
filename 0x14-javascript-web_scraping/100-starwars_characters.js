#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const resp = JSON.parse(body);

  for (const i of resp.characters) {
    request.get(i, (err, _, body) => {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});

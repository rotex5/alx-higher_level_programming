#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, function (error, _, body) {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body);

  const users = {};

  for (const i of json) {
    if (i.completed) {
      if (users[i.userId] == null) {
        users[i.userId] = 0;
      }
      users[i.userId]++;
    }
  }
  console.log(users);
});

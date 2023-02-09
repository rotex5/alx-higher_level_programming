#!/usr/bin/node

const request = require('request');

const url = 'https://jsonplaceholder.typicode.com/todos';

request.get(url, function (error, _, body) {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body);

  const users = {};

  for (const i of json) {
    if (i.completed === true) {
      if (users[i.userId] === undefined) {
        users[i.userId] = 0;
      }
      users[i.userId]++;
    }
  }
  console.log(users);
});

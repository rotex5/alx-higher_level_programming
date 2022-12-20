#!/usr/bin/node

function addMeMaybe (num, func) {
  num++;
  return func(num);
}

module.exports = {
  addMeMaybe: addMeMaybe
};

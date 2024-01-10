#!/usr/bin/node

let cur = 0;
exports.logMe = function (item) {
  console.log(`${cur}: ${item}`);
  cur++;
};

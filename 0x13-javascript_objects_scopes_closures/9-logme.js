#!/usr/bin/node

let argv = 0;
exports.logMe = function (item) {
  console.log(`${argv}: ${item}`);
  argv++;
};

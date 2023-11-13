#!/usr/bin/node
const [_, __, arg] = process.argv;

if (!arg) {
  console.log('No argument');
} else {
  console.log(arg);
}

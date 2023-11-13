#!/usr/bin/node
/* const [_, __, arg] = process.argv; */

if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}

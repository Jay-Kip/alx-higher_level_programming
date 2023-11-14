#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const array = process.argv.slice(2).map(Number);
  const num = array.sort((a, b) => b - a);
  console.log(num[1]);
}

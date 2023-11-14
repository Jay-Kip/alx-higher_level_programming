#!/usr/bin/node

if (!process.argv[2] || isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  const q = Number(process.argv[2]);
  let i = 0;

  while (i < q) {
    console.log('C is fun');
    i++;
  }
}

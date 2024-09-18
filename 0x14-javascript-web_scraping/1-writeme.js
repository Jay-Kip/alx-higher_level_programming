#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];
const dataToWrite = process.argv[3];

fs.writeFile(filepath, dataToWrite, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});

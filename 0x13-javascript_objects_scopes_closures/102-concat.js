#!/usr/bin/node

const fs = require('fs');

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFile = process.argv[4];

/* Read contents in the first file */
const fileContents1 = fs.readFileSync(sourceFilePath1, 'utf8');

/* Read contents in second file */
const fileContents2 = fs.readFileSync(sourceFilePath2, 'utf8');

/* Concatinate contents of the file */
const destConcat = fileContents1 + fileContents2;

/* Write to destination file */
fs.writeFileSync(destinationFile, destConcat);
